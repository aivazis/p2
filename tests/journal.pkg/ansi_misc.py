# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Check a few of the canonical X11 color names
    """
    # access the color map
    from j2.ANSI import ANSI
    # and the control sequence generator
    from j2.CSI import CSI

    # verify the contents of the {gray} color table
    # the reset sequence
    assert ANSI.misc("normal") == CSI.reset()

    assert ANSI.misc("amber") == CSI.csi24(0xff, 0xbf, 0x00)
    assert ANSI.misc("sage") == CSI.csi24(176, 208, 176)

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
