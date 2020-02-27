# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# mix in that generates an event on value change
class Dependency:
    """
    Mix-in class that enables a node to notify its observers when its value changes
    """


    # value management
    def setValue(self, value):
        """
        Override the value setter to notify my observers that my value changed
        """
        # pass the value along
        super().setValue(value)
        # notify my observers
        self.flush()
        # all done
        return self


# end of file
