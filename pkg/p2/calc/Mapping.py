# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


# base class for implementing associative containers
class Mapping:
    """
    Mix-in class that forms the basis of the representation of mappings
    """


    # constants
    category = "mapping"


    # interface
    @property
    def operands(self):
        """
        Build a sequence of my direct dependents
        """
        # return the mapping values
        return self._operands.values()


    @operands.setter
    def operands(self, operands):
        """
        Adjust my operands
        """
        # process the incoming mapping and save
        self._operands = self._container(self._ingest(operands=operands))
        # all done
        return


    # value management
    def getValue(self):
        """
        Compute and return my value
        """
        # return a container with the value of each operand; do not be tempted to avoid
        # realizing the container: value memoization will store the generator, it will get
        # exhausted on first read, and the value of the sequence will be empty thereafter!
        return self._container((key, op.getValue()) for key,op in self._operands.items())


    def setValue(self, value):
        """
        Set my value
        """
        # convert and store
        self.operands = value
        # all done
        return


    # metamethods
    def __init__(self, value, **kwds):
        # chain up
        super().__init__(operands=value, **kwds)
        # all done
        return


    # implementation details
    def _ingest(self, operands):
        """
        Convert {operands} into a mapping to nodes
        """
        for key, value in operands:
            # if {value} is not a node
            if not isinstance(value, self.node):
                # make it
                value = self.literal(value=value)
            # hand the pair off
            yield key, value
        # all done
        return

    # types
    _container = None # force subclasses to choose



# end of file
