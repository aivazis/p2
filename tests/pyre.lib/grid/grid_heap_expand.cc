// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// support
#include <cassert>
// get the grid
#include <p2/grid.h>


// a matrix is a rank-2 grid on the heap, packed in column major order
using matrix_t = pyre::grid::grid_t<pyre::grid::canonical_t<2>, pyre::memory::heap_t<double>>;


// example from the spectral expansion step of {ampcor}
int main(int argc, char * argv[]) {
    // initialize the journal
    pyre::journal::init(argc, argv);
    pyre::journal::application("grid_heap_expand");
    // make a channel
    pyre::journal::debug_t channel("pyre.grid.heap");

    // pick a dimension for the base arrat
    const auto dim = 8;
    // our base array is {dim x dim}
    matrix_t::shape_type shape { dim,dim };
    // it is packed in column major order with origin at {0,0}
    matrix_t::packing_type layout { shape };
    // make the base matrix
    matrix_t base { layout, layout.capacity() };

    // we want to fill each quadrant with different values, so let's start be defining "quadrant"
    auto quad = shape / 2;  // <- this is {dim/2, dim/2}

    // the top left quadrant starts at {0,0}
    auto tl = layout.box( {0,0}, quad );
    // loop over it
    for (auto idx : tl ) {
        // and set each entry
        base[idx] = 1;
    }

#if WRITE_IT_OUT_EXPLICITLYj
    // the top right quadrant starts at {0,dim/2}
    auto tr = layout.box( {0,dim/2}, quad );
    // loop over it
    for (auto idx : tr ) {
        // and set each entry
        base[idx] = 2;
    }

    // the bottom left quadrant starts at {dim/2,0}
    auto bl = layout.box( {dim/2,0}, quad );
    // loop over it
    for (auto idx : bl ) {
        // and set each entry
        base[idx] = 3;
    }

    // the bottom right quadrant starts at {dim/2,dim/2}
    auto br = layout.box( {dim/2,dim/2}, quad );
    // loop over it
    for (auto idx : br ) {
        // and set each entry
        base[idx] = 4;
    }
#else
    // go through the four quadrants
    for (auto t=0; t<2; ++t) {
        for (auto b=0; b<2; ++b) {
            // describe the restricted index range
            auto box = layout.box( {t*dim/2, b*dim/2}, quad );
            // loop over it
            for (auto idx : box) {
                // and set the value
                // base[idx] = 2*t + b + 1;
                base[idx] = layout[idx] + 1; // add some spice
            }
        }
    }
#endif

    // show me {base}
    channel << "base:" << pyre::journal::newline;
    for (size_t i=0; i<shape[0]; ++i) {
        for (size_t j=0; j<shape[1]; ++j) {
            channel << "  " << std::setw(2) << base[{i,j}];
        }
        channel << pyre::journal::newline;
    }
    channel << pyre::journal::endl;

    // now for the expanded array; its layout is {2*dim, 2*dim}
    auto expandedShape = 2 * shape;
    // it is also packed in column major order with origin at {0,0}
    matrix_t::packing_type expandedLayout { expandedShape };
    // instantiate
    matrix_t expanded { expandedLayout, expandedLayout.capacity() };
    // zero it out
    for (auto & cell : expanded) {
        cell = 0;
    }

    // go through the four quadrants
    for (auto t=0; t<2; ++t) {
        for (auto b=0; b<2; ++b) {
            // the source
            matrix_t::index_type src { t*dim/2, b*dim/2 };
            // the shift to the destination
            matrix_t::index_type shift { t*dim, b*dim };
            // copy
            for (auto idx : layout.box(src, quad)) {
                expanded[idx + shift] = base[idx];
            }
        }
    }

    // show me {expanded}
    channel << "expanded:" << pyre::journal::newline;
    for (size_t i=0; i<expandedShape[0]; ++i) {
        for (size_t j=0; j<expandedShape[1]; ++j) {
            channel << "  " << std::setw(2) << expanded[{i,j}];
        }
        channel << pyre::journal::newline;
    }
    channel << pyre::journal::endl;

    // nothing to do
    return 0;
}


// end of file
