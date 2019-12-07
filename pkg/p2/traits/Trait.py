# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


class Trait:
    """
    The base class for configurable component attributes

    Traits extend the notion of the a class attribute to an object that captures meta-data that
    has no natural resting place in a regular class declaration.

    Traits enable end-user configurable state, for both simple attributes and reference to more
    elaborate object, such as other components. Collectively, such attributes from the
    component inventory. Inventory items have names that connect them to the configuration
    store, per-instance storage for the attribute value, and additional meta-data, such as type
    information, reasonable default values, constraints and validators, documentation, and
    anything else the author of a component deems necessary.
    """


    # public data
    # the canonical name of the trait; it has to obey python identifier rules
    name = None
    # the default value of the trait, to be used in the absence of any other setting
    default = None
    # a set of alternative names for the trait; aliases are not required to satisfy the python
    # identifier tules
    aliases = None


    # framework hooks
    def bind(self, **kwds):
        """
        Notification that the {component} class that owns this trait has become aware of it
        """
        # by default, there's nothing to do; subclasses may override and chain up to here
        return self


    # meta-methods
    def __init__(self, name=name, default=default, **kwds):
        # chain up
        super().__init__(**kwds)
        # record the name
        self.name = name
        # set the default value
        self.default = default
        # initialize the aliases
        self.aliases = { name } if name is not None else set()
        # all done
        return


    def __set_name__(self, cls, name):
        """
        Invoked by the interpreter when it discovers a descriptor in a class declaration
        """
        # save my name
        self.name = name
        # and add it to the list of aliases
        self.aliases.add(name)
        # all done
        return


    def __get__(self, instance, cls):
        """
        Invoked by the interpreter to retrieve the value of a trait
        """


    def __set__(self, instance, value):
        """
        Invoked by the interpreter to assign a value to a trait
        """


# end of file
