// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_grid_OrderIterator_h)
#define pyre_grid_OrderIterator_h


// an iterator that enables visiting product ranks in a specific order
template <class productT, class orderT, bool isConst>
class pyre::grid::OrderIterator : public base_order_iterator<productT, isConst> {
    // types
public:
    // aliases for my template parameters
    using product_type = productT;
    using order_type = orderT;
    // aliases for me
    using iterator = OrderIterator<product_type, order_type, isConst>;
    using iterator_reference = iterator &;
    // my parts
    using product_reference = std::conditional_t<isConst, const product_type &, product_type &>;
    using order_const_iterator = typename order_type::const_iterator;
    using order_const_iterator_reference = const order_const_iterator &;
    // what i point to
    using value_type = typename product_type::value_type;
    using value_reference = std::conditional_t<isConst, const value_type &, value_type &>;

    // metamethods
public:
    constexpr OrderIterator(product_reference, order_const_iterator_reference);

    // iterator protocol
public:
    constexpr auto operator*() const -> value_reference;
    constexpr auto operator++() -> iterator_reference;

    // accessors: needed for the implementation of {operator==}
public:
    constexpr auto product() const -> product_reference;
    constexpr auto order() const -> order_const_iterator_reference;

    // implementation details: data
private:
    product_reference _product;
    order_const_iterator _order;
    // default metamethods
public:
    // destructor
    ~OrderIterator() = default;
    // let the compiler write the rest
    constexpr OrderIterator(const OrderIterator &) = default;
    constexpr OrderIterator(OrderIterator &&) = default;
    constexpr OrderIterator & operator=(const OrderIterator &) = default;
    constexpr OrderIterator & operator=(OrderIterator &&) = default;
};


// get the inline definitions
#define pyre_grid_OrderIterator_icc
#include "OrderIterator.icc"
#undef pyre_grid_OrderIterator_icc


#endif

// end of file
