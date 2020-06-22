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
template <pyre::grid::size_t N, template <typename, size_t> class containerT>
class pyre::grid::Order : public Rep<size_t, N, containerT> {
    // types
public:
    // alias for me
    using order_type = Order<N, containerT>;
    // my representation
    using size_type = decltype(N);
    using rep_type = Rep<size_t, N, containerT>;

    // metamethods
public:
    // aggregate initialization
    template <typename... argT>
    constexpr explicit Order(argT...);

    // static interface: factories
public:
    // row major: the sequence [N-1, ..., 0]
    static constexpr auto rowMajor() -> order_type;
    // and its alias
    static constexpr auto c() -> order_type;

    // column major: the sequence [0, ..., N-1]
    static constexpr auto columnMajor() -> order_type;
    // and its alias
    static constexpr auto fortran() -> order_type;

    // default metamethods
public:
    // destructor
    ~Order() = default;
    // constructors
    Order(const Order &) = default;
    Order(Order &&) = default;
    Order & operator=(const Order &) = default;
    Order & operator=(Order &&) = default;

    // implementation details: helpers
private:
    // the {columnMajor} helper
    template <size_t... seq>
    static constexpr auto
    _columnMajor(std::index_sequence<seq...>) -> order_type;

    // the {rowMajor} helper
    template <size_t... seq>
    static constexpr auto
    _rowMajor(std::index_sequence<seq...>) -> order_type;
};


// get the inline definitions
#define pyre_grid_Order_icc
#include "Order.icc"
#undef pyre_grid_Order_icc


#endif

// end of file
