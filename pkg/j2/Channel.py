# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# externals
import traceback       # location information
# framework
import p2              # for my superclass

# the index
from .Index import Index
# the base inventory
from .Inventory import Inventory
# the keeper of the global settings
from .Chronicler import Chronicler


# access to the channel shared state
class Channel(p2.patterns.named):
    """
    Encapsulation of the per-channel shared state

    All channels of a given severity that have the same name access a common state object. This
    enables a type of context-free control of a channel: anybody with access to the name of a
    channel can control whether it's active, or what device it writes to.
    """


    # types
    from .exceptions import JournalError


    # public data
    verbosity = 1           # default verbosity


    # access to settings from my shared inventory
    @property
    def state(self):
        """
        Get my activation state
        """
        # ask my inventory
        return self.inventory.state

    @state.setter
    def state(self, state):
        """
        Set my activation state
        """
        # adjust my inventory
        self.inventory.state = state
        # all done
        return


    @property
    def fatal(self):
        """
        Check whether i'm fatal
        """
        # ask my inventory
        return self.inventory.fatal

    @fatal.setter
    def fatal(self, fatal):
        """
        Mark me as {fatal}
        """
        # adjust my inventory
        self.inventory.fatal = fatal
        # all done
        return


    @property
    def device(self):
        """
        Get my device
        """
        # ask my inventory
        device = self.inventory.device
        # if it's non-trivial
        if device is not None:
            # that's the one
            return device
        # otherwise, return whatever the chronicler keeps
        return self.chronicler.device

    @device.setter
    def device(self, device):
        """
        Set my device
        """
        # hand it to my inventory
        self.inventory.device = device
        # all done
        return


    # control over the severity wide device
    @classmethod
    def getDefaultDevice(cls):
        """
        Get the default device associated with all channels of this severity
        """
        # my inventory type has it
        return cls.inventory_type.device


    @classmethod
    def setDefaultDevice(cls, device):
        """
        Get the default device associated with all channels of this severity
        """
        # get the previous setting
        old = cls.inventory_type.device
        # my inventory type has it
        cls.inventory_type.device = device
        # all done
        return old


    # access to information from my current buffer
    @property
    def page(self):
        """
        Return the contents of my buffer
        """
        # ask and pass on
        return self.buffer.page


    @property
    def meta(self):
        """
        Return the metadata of the current message
        """
        # ask and pass on
        return self.buffer.meta


    # interface
    def activate(self):
        """
        Enable the recording of messages
        """
        # easy
        self.state = True
        # all done
        return self


    def deactivate(self):
        """
        Disable the recording of messages
        """
        # easy
        self.state = False
        # all done
        return self


    def line(self, message=""):
        """
        Add {message} to the current page
        """
        # add message to my page
        self.page.append(message)
        # all done
        return self


    def log(self, message=None):
        """
        Add {message} to the current page and then record the entry
        """
        # if there is a final {message} to process
        if message is not None:
            # add it to the page
            self.page.append(message)

        # get a stack trace
        trace = traceback.extract_stack(limit=2)
        # so we can extract location information
        filename, line, function, *_ = trace[0]

        # decorate my current metadata
        meta = self.meta
        # with location information
        meta["filename"] = filename
        meta["line"] = line
        meta["function"] = function


        # certain channels, e.g. errors and firewalls, raise exceptions as part of committing a
        # message to the journal. such exceptions may be caught and handled, and the channel
        # instance may continue to be used. this leads to text accumulating on my page, and the
        # next time i'm flushed, my {buffer} still contains lines from the previous
        # message. the awkward block that follows attempts to prevent this by catching
        # exceptions, cleaning up the {buffer} in the finally section, and re-raising the
        # exception. of course, if no exception is raised, we just clean up the page and move
        # on

        # carefully
        try:
            # commit the message to the journal
            self.commit()
        # if i'm a fatal diagnostic, {commit} raises a journal exception
        except self.JournalError:
            # no worries; someone else may know what to do
            raise
        # but in any case
        finally:
            # flush my buffer
            self.buffer = self.newBuffer()

        # all done
        return self


    # metamethods
    def __init__(self, name, verbosity=verbosity, **kwds):
        # chain up
        super().__init__(name=name, **kwds)

        # set my verbosity
        self.verbosity = verbosity
        # look up my inventory
        self.inventory = self.index.lookup(name)
        # start out with an empty buffer
        self.buffer = self.newBuffer()
        # and an invalid locator
        self.locator = None

        # all done
        return


    @classmethod
    def __init_subclass__(cls, active=True, fatal=False, **kwds):
        # chain up
        super().__init_subclass__(**kwds)

        # we will derive a customized class with a synthesized name
        name = cls.__name__ + Inventory.__name__
        # that is a subclass of {Inventory}
        bases = [ Inventory ]
        # with default values for the channel state
        attributes = {
            "state": active,
            "fatal": fatal,
            "device": None
            }
        # build the class
        inventory = type(name, tuple(bases), attributes)
        # fix the module so it gets the correct attribution in stack traces
        inventory.__module__ = cls.__module__
        # attach it as the inventory type
        cls.inventory_type = inventory

        # create one using my inventory type
        index = Index(inventoryType=inventory)
        # and attach it
        cls.index = index

        # all done
        return


    def __bool__(self):
        """
        Simplify state testing
        """
        return self.inventory.state


    # implementation details
    def commit(self):
        """
        Commit the accumulated message to my device and flush
        """
        # if i'm not active
        if not self.state:
            # nothing to do
            return self

        # if my verbosity exceeds the maximum
        if self.verbosity > self.chronicler.verbosity:
            # nothing to do
            return self

        # record the entry
        self.record()

        # if i'm fatal
        if self.fatal:
            # get my metadata
            meta = self.meta
            # pull the location information
            filename = meta["filename"]
            line = meta["line"]
            function = meta["function"]
            # build a locator
            self.locator = p2.tracking.script(source=filename, line=line, function=function)
            # generate an exception
            raise self.fatalError(channel=self)

        # all done
        return self


    def record(self):
        """
        Write the accumulated message to the device
        """
        # subclasses must override
        raise NotImplementedError(f"class '{type(self).__name__}' must implement 'record'")


    def newBuffer(self):
        """
        Create a fresh message buffer
        """
        # initialize my metadata
        meta = {
            "channel": self.name,
            "severity": self.severity,
            }

        # inject whatever metadata it has
        meta.update(self.chronicler.meta)

        # get the buffer factory
        from .Buffer import Buffer
        # make one
        buffer = Buffer(meta=meta)

        # and return it
        return buffer


    # class data
    severity = "generic"           # the severity name
    chronicler = Chronicler()      # the keeper of the global settings
    fatalError = JournalError      # the exception i raise when i'm fatal
    inventory_type = Inventory     # the default inventory type; subclasses get their own
    index = Index(inventory_type)  # the severity wide channel index

    # instance data
    buffer = None                  # the accumulator of message content and metadata
    locator = None                 # location information
    inventory = None               # the state shared by all instances of the same name/severity


# end of file
