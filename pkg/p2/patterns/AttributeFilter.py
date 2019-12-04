# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# superclass
from .Type import Type


# declaration
class AttributeFilter(Type):
    """
    A base meta-class that enables attribute classification.

    A common pattern in pyre is to define classes that contain special attributes that collect
    declarative meta-data. These attributes are processed by special purpose meta-classes and
    are converted into appropriate behavior. For example, components have properties, which are
    decorated descriptors that enable external configuration of component state. Similarly, XML
    parsing happens with the aid of classes that capture the syntax, semantics and processing
    behavior of tags by employing descriptors to capture the layout of an XML document.
    """


    # interface
    @classmethod
    def pyre_harvest(cls, attributes, descriptor, reserved=None):
        """
        Examine the class {attributes}, looking for instances of {descriptor}
        """
        # reserved names are excluded from harvesting
        reserved = reserved if reserved is not None else cls.pyre_reserved
        # go through the attributes
        for name, attribute in attributes.items():
            # if this is a {descriptor} instance that;s not the in the reserved list
            if isinstance(attribute, descriptor) and name not in reserved:
                # pass it on
                yield name, attribute
        # all done
        return


    # public data
    # names excluded from filtering
    pyre_reserved = set()


# end of file
