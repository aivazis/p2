#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


def test():
    """
    Verify that the protocol family name is recorded and used correctly
    """
    # the protocol superclass
    from p2.components.Protocol import Protocol
    # and the dashboard
    from p2.framework.Dashboard import Dashboard

    # get the dashboard
    dashboard = Dashboard()
    # ask it for the protocol registrar
    registrar = dashboard.registrar


    # a protocol
    class Public(Protocol, family="tests.protocols.public"):
        """
        A public protocol
        """

        # storage for the phase markers
        phases = []

        # the hooks
        @classmethod
        def pyre_classRegistered(cls):
            """
            Hook that gets invoked by the framework after the class record has been registered but
            before any configuration events
            """
            # leave a bread crumb
            cls.phases.append(1)
            # chain up
            return super().pyre_classRegistered()


        @classmethod
        def pyre_classConfigured(cls):
            """
            Hook that gets invoked by the framework after the class record has been configured,
            before any instances have been created
            """
            # leave a bread crumb
            cls.phases.append(2)
            # chain up
            return super().pyre_classConfigured()


        @classmethod
        def pyre_classInitialized(cls):
            """
            Hook that gets invoked by the framework after the class record has been initialized,
            before any instances have been created
            """
            # leave a bread crumb
            cls.phases.append(3)
            # chain up
            return super().pyre_classInitialized()


    # verify that the phase hooks were called in the correct order
    assert Public.phases == [ 1,2,3 ]


    # all done
    return Public


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
