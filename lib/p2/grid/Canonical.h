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
template <pyre::grid::size_t N, template <typename, size_t> class containerT>
class pyre::grid::Canonical {
    // types
public:
    // alias for me
    using canonical_type = Canonical<N, containerT>;
    // the sizes of things
    using size_type = size_t;
    // my parts
    // rank order
    using order_type = Order<containerT<size_type, N>>;
    // rank specifications
    using shape_type = Shape<containerT<size_type, N>>;
    // indices
    using index_type = Index<containerT<int, N>>;
    // strides are like shapes with a wide type so overflow is less likely
    using strides_type = Shape<containerT<size_type, N>>;
    // offsets
    using difference_type = typename index_type::difference_type;
    // iterators
    using index_iterator = IndexIterator<canonical_type>;

    // metamethods
public:
    // constructor that deduces {_strides} and {_nudge}
    constexpr explicit
    Canonical(const shape_type & shape,
              const index_type & origin = index_type::zero(),
              const order_type & order = order_type::c());
    // constructor that requires a detailed description of the packing; useful for making slices
    constexpr
    Canonical(const shape_type & shape,
              const index_type & origin,
              const order_type & order,
              const strides_type & strides,
              difference_type nudge);

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

    // mutators: {canonical_type} instances are {const}, so mutators create new instances
public:
    constexpr auto order(const order_type &) const -> canonical_type;

    // the packing isomorphism
public:
    // from a given offset to the matching index
    constexpr auto index(difference_type) const -> index_type;
    // from an index to its offset from the beginning of the array
    constexpr auto offset(const index_type &) const -> difference_type;

    // syntactic sugar for the above
    constexpr auto operator[](difference_type) const -> index_type;
    constexpr auto operator[](const index_type &) const -> difference_type;

    // slicing
public:
    // when the shape is known at compile time
    template <size_t... shape>
    constexpr auto cslice(const index_type & base) const;
    // when only the rank of the slice is known at compile time
    template <size_t sliceRank = N>
    constexpr auto slice(const shape_type & shape, const index_type & base) const;

    // iteration support: iterators generate sequences of indices
public:
    constexpr auto begin() const -> index_iterator;
    constexpr auto end() const -> index_iterator;

    // static interface
public:
    static constexpr auto rank() -> size_type;

    // implementation details: static helpers
protected:
    // given a {shape} and an {order}, infer the axis strides assuming tight packing
    static constexpr auto strides(const shape_type &, const order_type &) -> strides_type;
    // given the packing {strides}, project an {index} to an offset such that the {zero} index
    // maps to offset 0
    static constexpr auto project(const index_type &, const strides_type &) -> difference_type;

    // implementation details: data
private:
    // supplied by the caller
    const shape_type _shape;         // my shape
    const order_type _order;         // the packing order of the axes
    const index_type _origin;        // the smallest allowable index value
    // deduced
    const strides_type _strides;     // the vector of strides for axis
    const difference_type _nudge;    // offset correction when {_origin} is not {zero}

    // metamethods with default implementations
public:
    // destructor
    ~Canonical() = default;
    // constructors
    constexpr Canonical(const Canonical &) = default;
    constexpr Canonical & operator= (const Canonical &) = default;
    constexpr Canonical(Canonical &&) = default;
    constexpr Canonical & operator= (Canonical &&) = default;
};


// get the inline definitions
#define pyre_grid_Canonical_icc
#include "Canonical.icc"
#undef pyre_grid_Canonical_icc


#endif

// end of file
