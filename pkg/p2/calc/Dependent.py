# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# declaration
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
        # chain up to change the value; my super-classes may not implement
        super().setValue(value)
        # start observing again
        self.observe(self.operands)
        # all done
        return self


    # meta-methods
    def __init__(self, operands, **kwds):
        # assume i am a composite
        super().__init__(operands=operands, **kwds)
        # observe my operands
        self.observe(observables=self.operands)
        # all done
        return


# end of file
