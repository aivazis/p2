# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


# superclass
from .Configurable import Configurable
# metaclass
from .Role import Role


# declaration
class Protocol(Configurable, metaclass=Role):
    """
    The base class for requirement specifications
    """


    # type id
    pyre_isProtocol = True


    # compatibility checks
    @classmethod
    def pyre_isCompatibleWith(cls, spec, fast=True):
        """
        Check whether this protocol is compatible with {spec}
        """
        # i'm never compatible with components
        if spec.pyre_isComponent:
            # in fact, let's treat asking the question as a bug
            import journal
            # build a description
            msg = "PC compatibility checks are not supported"
            # complain
            raise journal.firewall("pyre.components").log(msg)
        # chain up for the basic checks
        report = super().pyre_isCompatibleWith(spec=spec, fast=fast)
        # and report any errors
        return report


    @classmethod
    def pyre_isTypeCompatibleWith(cls, protocol):
        """
        Decide whether {cls} is type compatible with the given {protocol}

        Here, we deal with a stricter question than general assignment compatibility. The
        question is whether a component that implements {cls} is a good candidate for a role
        specified by {protocol}. In general, this is a hard question to answer, and depends
        strongly on the {protocol} design.

        The baseline implementation here is based on pedigree comparisons. Descendants can
        provide their own interpretation of the question.
        """

        # i am compatible with my ancestors
        if issubclass(cls, protocol):
            # so go no further
            return True

        # previously, there was code here that implemented inheritance tests based on public
        # keys, ostensibly to accommodate cases where inheritance relationships were disguised
        # by the technique that was used to import components dynamically from the filesystem;
        # i may need to revisit this when i have test cases that fail

        # if we get this far, we have a problem
        return False


# end of file
