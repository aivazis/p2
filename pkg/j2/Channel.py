# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# framework
import p2              # for my superclass
# access to the global settings
from .Chronicler import Chronicler
# and my index
from .Index import Index


# access to the channel shared state
class Channel(p2.patterns.named):
    """
    Encapsulation of the per-channel shared state

    All channels of a given severity that have the same name access a common state object. This
    enables a type of context-free control of a channel: anybody with access to the name of a
    channel can control whether it's active, or what device it writes to.
    """


    # public data
    @property
    def state(self):
        """
        Get my current activation state
        """
        # my inventory knows...
        return self.inventory.state


    @state.setter
    def state(self, state):
        """
        Set my current activation state
        """
        # save the new {state} into the shared inventory
        self.inventory.state = state
        # all done
        return


    @property
    def device(self):
        """
        Get my current output device
        """
        # there may be one attached to me
        device = self.inventory.device
        # if it's there
        if device:
            # that's the one
            return device
        # there may be one attached to all channels of my severity
        device = self.defaultDevice
        # if it's there
        if device:
            # that's the one
            return device
        # otherwise, return the global one attached to the chronicler
        return self.chronicler.device


    @device.setter
    def device(self, device):
        """
        Set my output device
        """
        # interpret this as setting the per channel device
        self.inventory.device = device
        # all done
        return


    # access to severity wide configuration
    @classmethod
    def getDefaultDevice(cls):
        # easy enough
        return cls.defaultDevice


    @classmethod
    def setDefaultDevice(cls, device):
        # save the current device
        old = cls.defaultDevice
        # install the new one
        cls.defaultDevice = device
        # and return the old
        return old


    # interface
    def activate(self):
        """
        Enable output generation
        """
        # delegate to my inventory
        self.inventory.state = True
        # all done
        return self


    def deactivate(self):
        """
        Enable output generation
        """
        # delegate to my inventory
        self.inventory.state = False
        # all done
        return self


    # metamethods
    def __init__(self, name, **kwds):
        # chain up
        super().__init__(name=name, **kwds)
        # look up my inventory
        self.inventory = self.index.lookup(name)
        # all done
        return


    @classmethod
    def __init_subclass__(cls, /, inventory_type, **kwds):
        # chain up
        super().__init_subclass__(**kwds)
        # attach the inventory type
        cls.inventory_type = inventory_type
        # create an index
        index = Index(inventory_type)
        # and attach it
        cls.index = index
        # all done
        return


    def __bool__(self):
        """
        Simplify state testing
        """
        return self.state


    # implementation details
    # data
    inventory = None

    # class data; managed by class methods
    index = None               # the severity wide channel index; patched during bootstrapping
    defaultDevice = None       # the severity wide device
    chronicler = Chronicler()  # the singleton with the global journal configuration


    # inventory types for the various channels
    class inventory_type:
        """
        The base inventory
        """

        # public data
        state = None
        device = None

        # interface
        def copy(self, source):
            """
            Make me look like {source}
            """
            # easy
            self.state = source.state
            self.device = source.device
            # all done
            return


    class enabled_type(inventory_type):
        """
        Inventory for channels that are activated by default, i.e. warnings, errors, and firewalls
        """

        # public data
        state = True


    class disabled_type(inventory_type):
        """
        Inventory for channels that are deactivated by default, i.e. info, and debug
        """

        # public data
        state = False


    class fatal_type(inventory_type):
        """
        Inventory for channels that can raise an exception when they tigger, i.e. firewalls
        """

        # public data
        fatal = True

        # interface
        def copy(self, source):
            """
            Make me look like {source}
            """
            # chain up
            super().copy(source)
            # copy whether i'm fatal
            self.fatal = source.fatal
            # all done
            return


    class enabled_fatal_type(enabled_type, fatal_type):
        """
        Inventory for channels that are enabled and fatal
        """


    class disabled_fatal_type(disabled_type, fatal_type):
        """
        Inventory for channels that are disabled and fatal
        """


# end of file
