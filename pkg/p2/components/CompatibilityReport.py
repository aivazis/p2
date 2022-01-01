# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


# externals
import collections

# declaration
class CompatibilityReport:


    # public data
    component = None
    specification = None

    @property
    def isClean(self):
        """
        Check whether there are any incompatibilities to report
        """
        # check the pile
        return not self.incompatibilities


    # metamethods
    def __init__(self, component, specification, clean=isClean, **kwds):
        # chain up
        super().__init__(**kwds)
        # record the pair i report on
        self.component = component
        self.specification = specification
        # initialize my list of incompatibilities
        self.incompatibilities = collections.defaultdict(list)
        # all done
        return


    def __bool__(self):
        """
        Return {True} if there are no incompatibilities to report
        """
        # easy enough
        return self.isClean


# end of file
