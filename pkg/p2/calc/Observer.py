# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# the superclass
from .Reactor import Reactor
# the complement
from .Observable import Observable


# interface for dependency management
class Observer(Reactor):
    """
    Mix-in class that enables a node to be notified when the value of its dependents change
    """


    # interface
    def observe(self, observables):
        """
        Add me as an observer to all {observables}
        """
        # loop through {observables}
        for observable in observables:
            # skip the ones that are not observable
            if not isinstance(observable, Observable): continue
            # add me as an observer to the rest
            observable.addObserver(self)
        # all done
        return self


    def ignore(self, observables):
        """
        Stop observing the {observables}
        """
        # loop through {observables}
        for observable in observables:
            # skip the ones that are not observable
            if not isinstance(observable, Observable): continue
            # drop me as an observer from the rest
            observable.removeObserver(self)
        # all done
        return self


    # implementation details
    # alterations of the dependency graph
    def _substitute(self, current, replacement, **kwds):
        """
        Observe {replacement} instead of {current}
        """
        # chain up to handle other aspects of my relationship with the two nodes
        r = super()._substitute(current=current, replacement=replacement, **kwds)

        # if i'm in the list of observers of {current}
        if self in set(current.observers):
            # remove me
            current.removeObserver(observer=self)
            # additionally, if i'm  not the one being replaces
            if r is self:
                # add me as an observer to {replacement}
                replacement.addObserver(observer=self)

        # all done
        return r


# end of file
