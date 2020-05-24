// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_grid_h)
#define pyre_grid_h


// This package is an attempt to provide support for multidimensional arrays
// The name {grid} is the best I could do in order to avoid

// The problem is factored into independent parts:
//
// - storage: N cells of a known type are stored in a linear, contiguous memory expanse
//
// - indexing: an index is an n-tuple of values, where n is the dimensionality of the grid; the
//   indexing problem is equivalent to providing a map from an index to [0, N).


// publish the interface
// the api is in "grid/api.h"
#include "grid/public.h"


#endif

// end of file
