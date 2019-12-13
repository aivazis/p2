# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# declaration
class Public:
    """
    Mix-in class that endows descriptors with a name, aliases and documentation support
    """


    # public data
    # the canonical name of the trait; it has to obey python identifier rules
    name = None
    # a set of alternative names for the trait; aliases are not required to satisfy the python
    # identifier tules
    aliases = None
    # the docstring
    doc = ''
    # the trait purpose in a few words
    tip = ''


    # meta-methods
    def __init__(self, name=name, aliases=aliases, tip=tip, doc=doc, **kwds):
        # chain up
        super().__init__(**kwds)
        # record the name
        self.name = name
        # initialize the aliases
        self.aliases = aliases if aliases is not None else set()
        # if a name was supplied
        if name is not None:
            # add it to the aliases
            aliases.add(name)
        # record the help string
        self.doc = doc
        # and the tip
        self.tip = tip
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


# end of file
