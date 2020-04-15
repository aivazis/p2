# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# externals
# for my superclass
import p2
# for location information
import traceback


# encapsulation of message recording
class Diagnostic(p2.patterns.named):
    """
    Encapsulation of the message recoding machinery
    """


    # public data
    page = None       # the accumulated body of the message
    meta = None       # message metadata
    verbosity = 1     # the verbosity level; N.B.: per-instance, not per-channel
    locator = None    # access to locator information extracted from the message metadata


    # interface
    def line(self, message=""):
        """
        Add another line to the message page
        """
        # add {message} to my page
        self.page.append(message)
        # all done
        return self


    def log(self, message=None):
        """
        Add an optional line to the page and then record the entry
        """
        # if the optional {message} in not empty
        if message is not None:
            # add it to the page
            self.page.append(message)
        # get a stack trace
        trace = traceback.extract_stack(limit=2)
        # so we can extract location information
        filename, line, function, source = trace[0]

        # decorate my metadata
        meta = self.meta
        # with the location information
        meta["filename"] = filename
        meta["line"] = line
        meta["function"] = function
        meta["source"] = source

        # build my locator
        self.locator = p2.tracking.script(source=filename, line=line, function=function)

        # certain channels, e.g. the built-in error and firewall, raise exceptions as part of
        # committing a message to the journal. such exceptions may be caught and handled, and
        # the channel instance may continue to be used. this leads to text accumulating on my
        # page, and the next time i'm flushed, {page} still contains lines from the old
        # text. the awkward block that follows attempts to prevent this by catching exceptions,
        # cleaning up the {page} in the finally section, and re-raising the exception. of
        # course, if no exception is raised, we just clean up the page and move on

        # carefully
        try:
            # commit the message to the journal
            self.commit()
        # if i'm a fatal diagnostic, {commit} raises a journal exception
        except:
            # no worries; someone else may know what to do
            raise
        # but in any case
        finally:
            # flush the page
            self.page = []

        # all done
        return self


    # metamethods
    def __init__(self, name, verbosity=1, **kwds):
        # chain up
        super().__init__(name=name, **kwds)

        # save the verbosity; it is set on a per-instance basis, and not part of the shared state
        self.verbosity = verbosity

        # initialize my buffers
        # the content accumulator
        self.page = []
        # the metadata
        self.meta = {
            "channel": name,
            "severity": self.severity,
            }
        # the locator
        self.locator = None

        # all done
        return


# end of file
