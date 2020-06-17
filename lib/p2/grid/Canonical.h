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
    // my parts
    using index_type = Index<N>;
    using shape_type = Shape<N>;
    using order_type = Order<N>;

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
    constexpr auto shape() const -> shape_type;
    constexpr auto order() const -> order_type;
    constexpr auto origin() const -> index_type;
    constexpr auto nudge() const -> typename index_type::axis_type;


    // implementation details: data
private:
    shape_type _shape;     // my shape
    order_type _order;     // the packing order of the axes
    index_type _origin;    // the smallest allowable index value
    long _nudge;           // offset correction when {_origin} is not {zero}
};


// get the inline definitions
#define pyre_grid_Canonical_icc
#include "Canonical.icc"
#undef pyre_grid_Canonical_icc


#endif

// end of file
