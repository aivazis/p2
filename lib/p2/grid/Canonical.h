// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_grid_Canonical_h)
#define pyre_grid_Canonical_h


// encapsulation of the canonical packing strategy
// a packing strategy provides the isomorphism
//
//    Z_s1 x ... x Z_sn -> Z_(s1 * ... * sn)
//
template <pyre::grid::size_t N>
class pyre::grid::Canonical {
    // types
public:
    // alias for me
    using canonical_type = Canonical<N>;
    // the sizes of things
    using size_type = size_t;
    // my parts
    using index_type = Index<N, std::array>;
    using shape_type = Shape<N, std::array>;
    using order_type = Order<N, std::array>;
    // the array with the strides looks just like a shape
    using strides_type = shape_type;
    // offsets
    using difference_type = typename index_type::difference_type;
    // iterators
    using iterator_type = Iterator<canonical_type>;

    // metamethods
public:
    // destructor
    ~Canonical() = default;

    // constructor
    constexpr explicit Canonical(shape_type,
                                 index_type = index_type::zero(),
                                 order_type = order_type::c());

    // let the compiler take care of these
    constexpr Canonical(const Canonical &) = default;
    constexpr Canonical(Canonical &&) = default;
    constexpr Canonical & operator= (const Canonical &) = default;
    constexpr Canonical & operator= (Canonical &&) = default;

    // interface
public:
    // accessors
    // user supplied
    constexpr auto shape() const -> shape_type;
    constexpr auto order() const -> order_type;
    constexpr auto origin() const -> index_type;
    // deduced
    constexpr auto strides() const -> strides_type;
    constexpr auto nudge() const -> difference_type;

    // the total number of addressable cells
    constexpr auto capacity() const -> size_type;

    // the packing isomorphism
    constexpr auto index(difference_type) -> index_type;
    constexpr auto offset(const index_type &) -> difference_type;

    // iteration support: iterators generate sequences of indices
    constexpr auto begin() const;
    constexpr auto end() const;
    constexpr auto begin(const order_type &) const;

    // static interface
public:
    static constexpr auto dim() -> size_type;

    // implementation details: static helpers
protected:
    // given a {shape} and an {order}, infer the axis strides assuming tight packing
    static constexpr auto strides(const shape_type &, const order_type &) -> strides_type;
    // given the packing {strides}, project an {index} to an offset such that the {zero} index
    // maps to the origin
    static constexpr auto project(const index_type &, const strides_type &) -> difference_type;

    // implementation details: data
private:
    // supplied by the caller
    shape_type _shape;         // my shape
    order_type _order;         // the packing order of the axes
    index_type _origin;        // the smallest allowable index value
    // deduced
    shape_type _strides;       // the vector of strides for axis
    difference_type _nudge;    // offset correction when {_origin} is not {zero}
};


// get the inline definitions
#define pyre_grid_Canonical_icc
#include "Canonical.icc"
#undef pyre_grid_Canonical_icc


#endif

// end of file
