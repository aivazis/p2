// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_grid_Index_h)
#define pyre_grid_Index_h


// storage for a multidimensional index
// the representation is an {std::array} with {int} as the {value_type}
// other index abstraction must be reducible to this one so offsets can be computed
template <size_t N, bool checkBounds>
class pyre::grid::Index {
    // types
public:
    // the representation of my collection of values
    using rep_type = array_t<int, N>;
    // dependent types
    using size_type = typename rep_type::size_type;
    // the type of individual axis values
    using idx_type = typename rep_type::value_type;

    // metamethods
public:
    // destructor
    ~Index() = default;
    // constructor; a variadic template to enable initializer lists
    template <typename... argT>
    inline explicit Index(argT...);

    // static interface
public:
    inline static constexpr auto dim() -> size_type;

    // implementation details: data
private:
    rep_type _rep; // my values
};


// get the inline definitions
#define pyre_grid_Index_icc
#include "Index.icc"
#undef pyre_grid_Index_icc


#endif

// end of file
