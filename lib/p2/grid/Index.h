// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_grid_Index_h)
#define pyre_grid_Index_h


// storage for a multidimensional index
// the representation is an {std::array} with {int} as the {value_type}
// other index abstractions must be reducible to this one so offsets can be computed
template <size_t N, bool checkBounds>
class pyre::grid::Index {
    // types
public:
    // me
    using index_type = Index<N, checkBounds>;
    // the representation of my collection of values
    using rep_type = array_t<int, N>;
    // dependent types
    using size_type = typename rep_type::size_type;
    // individual axis values
    using idx_type = typename rep_type::value_type;
    using idx_reference = idx_type &;
    using idx_const_reference = const idx_type &;

    // metamethods
public:
    // destructor
    ~Index() = default;

    // constructor that fills an index with a given {value}
    inline constexpr explicit Index(idx_type);

    // constructor; a variadic template to enable initializer lists
    template <typename... argT>
    inline constexpr explicit Index(argT...);

    // access
    // read-only
    auto operator[](size_type axis) const -> idx_type;
    // read/write
    auto operator[](size_type axis) -> idx_reference;

    // iteration support
    auto begin() const;
    auto end() const;

    auto begin();
    auto end();

    // static interface
public:
    inline static constexpr auto dim();

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
