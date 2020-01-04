# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# declaration
class Chain:
    """
    A locator that ties together two others in order to express that something in {next}
    caused {this} to be recorded
    """


    # meta methods
    def __init__(self, this, next):
        # save the links
        self.this = this
        self.next = next
        # all done
        return


    def __str__(self):
        # if {next} is non-trivial
        if self.next:
        # show the chain
            return f"{self.this}, {self.next}"
        # otherwise don't
        return f"{self.this}"


    # implementation details
    __slots__ = "this", "next"


# end of file
