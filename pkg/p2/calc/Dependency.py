# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


# mix in that generates an event on value change
class Dependency:
    """
    Value management for observables
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
