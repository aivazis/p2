// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// support
#include <cassert>
// get the grid
#include <p2/grid.h>

// type alias
using product_t = pyre::grid::product_t<4>;


// exercise operator[]
int main()
{
    // at compile time
    constexpr product_t p_1 {0, 1, 2, 3};

    // verify the contents
    static_assert (p_1[0] == 0);
    static_assert (p_1[1] == 1);
    static_assert (p_1[2] == 2);
    static_assert (p_1[3] == 3);

    // make a writable one
    product_t p_2 { 0,0,0,0 };

    // set it
    p_2[0] = 0;
    p_2[1] = 1;
    p_2[2] = 2;
    p_2[3] = 3;

    // check it
    assert (p_2[0] == 0);
    assert (p_2[1] == 1);
    assert (p_2[2] == 2);
    assert (p_2[3] == 3);

    // all done
    return 0;
}


// end of file