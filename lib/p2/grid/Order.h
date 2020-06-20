// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_grid_Order_h)
#define pyre_grid_Order_h


// generalization to multiple dimensions of the familiar row-major and column-major order
// strategies. this is captured as a permutation in {S_N} that denotes the storage order of the
// indices.
template <pyre::grid::size_t N>
class pyre::grid::Order {
    // types
public:
    // alias for me
    using order_type = Order<N>;
    // my representation
    using size_type = decltype(N);
    using rep_type = array_t<size_t, N>;
    // individual ranks
    using rank_type = typename rep_type::value_type;
    using rank_reference = rank_type &;
    using rank_const_reference = const rank_type &;

    // metamethods
public:
    // destructor: let the compiler do it
    ~Order() = default;

    // a constructor that takes an initializer list
    template <typename... argT>
    constexpr explicit Order(argT...);

    // let the compiler write the rest
    Order(const Order &) = default;
    Order(Order &&) = default;
    Order & operator=(const Order &) = default;
    Order & operator=(Order &&) = default;

    // interface
public:
    // access
    // read only
    constexpr auto operator[](size_type) const -> rank_type;
    // read/write
    constexpr auto operator[](size_type) -> rank_reference;

    // iteration support
    // read only
    constexpr auto begin() const;
    constexpr auto end() const;
    // read/write
    constexpr auto begin();
    constexpr auto end();

    // static interface
public:
    static constexpr auto dim() -> size_type;

    // static interface: factories
public:
    // c-like: last index varies first, in order right to left
    static constexpr auto rowMajor();
    // and it alias
    static constexpr auto c();

    // fortran-like: first index varies first, in order left to right
    static constexpr auto columnMajor();
    // and its alias
    static constexpr auto fortran();

    // implementation details: data
private:
    rep_type _ranks;
};


// get the inline definitions
#define pyre_grid_Order_icc
#include "Order.icc"
#undef pyre_grid_Order_icc


#endif

// end of file
