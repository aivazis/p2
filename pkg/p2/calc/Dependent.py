# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


# the value management part of being an observer
class Dependent:
    """
    Mix-in class that enables a node to be notified when the values of its dependencies change
    """


    # value management
    def setValue(self, value):
        """
        Set my value
        """
        # stop observing my current operands
        self.ignore(self.operands)
        # chain up to change the value, which may involve replacing my {operands} entirely;
        # also, my super-classes may not implement, in which case this will raise an exception
        super().setValue(value)
        # start observing the new ones
        self.observe(self.operands)
        # all done
        return self


    # metamethods
    def __init__(self, **kwds):
        # assume i am a composite
        super().__init__(**kwds)
        # observe my operands
        self.observe(observables=self.operands)
        # all done
        return


# end of file
