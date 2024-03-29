# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


# superclasses
from .Trait import Trait
from ..descriptors.Descriptor import Descriptor


# declaration
class Behavior(Trait, Descriptor):
    """
    The base class for component methods that are part of the external interface
    """


    # framework data
    # my category name
    category = "behavior"
    # predicate that indicates this trait is a behavior
    isBehavior = True


    # metamethods
    def __new__(cls, method=None, **kwds):
        """
        Trap invocations with metadata and delay the decoration of the method
        """
        # if the {method} is known
        if method is not None:
            # verify that the user gave us something we can decorate
            assert callable(method), 'please invoke with keyword arguments'
            # and chain up to do the normal thing; swallow the extra arguments for now; they'll
            # become accessible again in {__init__}
            return super().__new__(cls)

        # if we don't know the {method} yet, the decorator was invoked with keyword arguments;
        # the strategy here is to return a {Behavior} constructor as the value of this
        # invocation. this accomplishes two things: it gives python something to call when the
        # method declaration is done, and it prevents my {__init__} from getting invoked
        # prematurely

        # make a constructor closure
        def build(method):
            """
            Convert a component method into a behavior
            """
            # just build one of my instances
            return cls(method=method, **kwds)

        # and hand it over
        return build


    def __init__(self, method, **kwds):
        # chain up
        super().__init__(doc=method.__doc__, **kwds)
        # save the method
        self.method = method
        # all done
        return


    # N.B.: this is a non-data descriptor; it shouldn't define either {__set__} or {__delete__}
    def __get__(self, instance, cls):
        """
        Invoked to retrieve the behavior
        """
        # let the encapsulated function object do the work
        return self.method.__get__(instance, cls)


    def __str__(self):
        # easy enough
        return f"'{self.name}', a behavior"


# end of file
