#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# externals
import collections  # for {defaultdict}


# verify we can derive from {Channel} and create independent channel factories
def test():
    """
    Verify there is no cross talk among the indices of different channel severities
    """

    # get the package
    from j2.Channel import Channel

    # three channel subclasses
    class info(Channel):
        """
        info channel
        """
        index = collections.defaultdict(Channel.disabled_type)

    class warning(Channel):
        """
        warning channel
        """
        index = collections.defaultdict(Channel.enabled_type)

    class error(Channel):
        """
        error channel
        """
        index = collections.defaultdict(Channel.enabled_fatal_type)

    # make a couple of info channels
    info_1 = info("info.channel_1")
    info_2 = info("info.channel_2")

    # make a couple of warning channels
    warning_1 = warning("warning.channel_1")
    warning_2 = warning("warning.channel_2")

    # make a couple of error channels
    error_1 = error("error.channel_1")
    error_2 = error("error.channel_2")

    # check the states
    assert info_1.state == False
    assert info_2.state == False
    assert warning_1.state == True
    assert warning_2.state == True
    assert error_1.state == True
    assert error_2.state == True

    # get the info index
    infos = info.index
    # verify it has exactly two registered names
    assert len(infos) == 2
    # that one of them is "info.channel_1"
    assert "info.channel_1" in infos
    # and the other is "info.channel_2"
    assert "info.channel_2" in infos

    # repeat with the warning index
    warnings = warning.index
    # verify it has exactly two registered names
    assert len(warnings) == 2
    # that one of them is "warning.channel_1"
    assert "warning.channel_1" in warnings
    # and the other is "warning.channel_2"
    assert "warning.channel_2" in warnings

    # repeat with the error index
    errors = error.index
    # verify it has exactly two registered names
    assert len(errors) == 2
    # that one of them is "error.channel_1"
    assert "error.channel_1" in errors
    # and the other is "error.channel_2"
    assert "error.channel_2" in errors

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
