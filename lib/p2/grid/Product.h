// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_grid_Product_h)
#define pyre_grid_Product_h


// thin wrapper over {rep_t} that serves as the base for all classes that encapsulate cartesian
// products, hence the name
//
// the client supplies:
//  - its rank {N}
//  - the category of each factor in {T}: {int}, {long}, {size_t}
//  - the container choice to hand down to {rep_t} that stores per-rank values
//
// note: no {crtp} here, for now...
template <class containerT>
class pyre::grid::Product : public Rep<containerT> {
    // types
public:
    // alias for my base
    using rep_type = Rep<containerT>;
    // the factor type determines the sets whose product we are computing
    using rank_type = typename rep_type::value_type;

    // metamethods
public:
    // constructor
    template <typename... argT>
    constexpr explicit Product(argT...);
};


// get the inline definitions
#define pyre_grid_Product_icc
#include "Product.icc"
#undef pyre_grid_Product_icc


#endif

// end of file
