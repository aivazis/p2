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

// compile time sanity check: make sure the header file is accessible
int main()
{
    // make an index
    product_t p { 0, 0, 0, 0 };

    // verify that the index dimensionality is reported correctly through the type
    static_assert(product_t::dim() == 4);
    // verify that the index dimensionality is reported correctly through an instance
    static_assert(p.dim() == 4);

    // every product is equal to itself
    assert (p == p);

    // make a different one
    product_t q { 1, 1, 1, 1 };
    // verify it's not the same as {q}
    assert (p != q);

    // all done
    return 0;
}


// end of file
