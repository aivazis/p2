# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


# externals
import weakref
# the superclas
from .Reactor import  Reactor


# support for keeping track and notifying observers
class Observable(Reactor):
    """
    Mix-in class that notifies its clients when the value of a node changes
    """

    # public data
    @property
    def observers(self):
        """
        Return an iterable over my live observers
        """
        # go through the references to my observers
        for ref in self._observers:
            # unwrap it
            observer = ref()
            # if it is dead
            if observer is None:
                # skip it
                continue
            # otherwise, send it along
            yield observer

        # all done
        return


    # observer management
    def addObserver(self, observer):
        """
        Add {observer} to my pile
        """
        # build a weak reference to {observer} and add it to the pile
        self._observers.add(weakref.ref(observer))
        # all done
        return self


    def removeObserver(self, observer):
        """
        Remove {observer} from my pile
        """
        # build a weak reference to {observer} and remove it from the pile
        self._observers.remove(weakref.ref(observer))
        # all done
        return self


    def replace(self, obsolete):
        """
        Remove {obsolete} from its upstream graph and assume its responsibilities
        """
        # chain up
        super().replace(obsolete=obsolete)
        # make a pile of nodes that have been adjusted
        clean = set()
        # go through the observers of {obsolete}; make a copy
        for observer in tuple(obsolete.observers):
            # {obsolete} is most likely an operand; perform a substitution
            observer.substitute(current=obsolete, replacement=self, clean=clean)
        # all done
        return self


    # signaling
    def flush(self, **kwds):
        """
        Handler of the notification event from one of my observables
        """
        # take this opportunity to clean up my observers
        observers = set(self.observers)
        # go through the pile
        for observer in observers:
            # notify each one
            observer.flush(observable=self)
        # rebuild the set of references
        self._observers = set(map(weakref.ref, observers))
        # chain up
        return super().flush(**kwds)


    # meta-methods
    def __init__(self, **kwds):
        # chain up
        super().__init__(**kwds)
        # initialize the set of my observers
        self._observers = set() # should have been a weak set, but I can do better...
        # all done
        return


    # implementation details
    # alterations of the dependency graph
    def _substitute(self, current, replacement, clean):
        """
        Replace {current} by {replacement}
        """
        # chain up
        r = super()._substitute(current=current, replacement=replacement, clean=clean)

        # as an observable, all i have to check is whether i got replaced
        if self is not r:
            # in which case, i must notify my observers
            self.flush()
        # all done
        return r


# end of file
