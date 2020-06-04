// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_grid_Product_h)
#define pyre_grid_Product_h

// thin wrapper over {std::array} that provides representation support for the other
// fundamental concepts in this package
template <pyre::grid::size_t N, typename factorT>
class pyre::grid::Product {
    // types
public:
    // the factor type determines the sets whose product we are computing
    using factor_type = factorT;
    // storage
    using rep_type = array_t<factor_type, N>;
    // dependent types
    using size_type = decltype(N);
    using factor_reference = factor_type &;
    using factor_const_reference = const factor_type &;

    // metamethods
public:
    // destructor; let the compiler write it
    ~Product() = default;

    // constructor
    template <typename... argT>
    constexpr explicit Product(argT...);

    // interface
public:
    // access
    // read only
    constexpr auto operator[](size_type) const -> factor_type;
    // read/write
    inline auto operator[](size_type) -> factor_reference;

    // iteration support
    // read only
    constexpr auto begin() const;
    constexpr auto end() const;
    // read/write
    inline auto begin();
    inline auto end();

    // static interface
public:
    static constexpr auto dim();

    // implementation details: data
private:
    rep_type _rep;
};

// get the inline definitions
#define pyre_grid_Product_icc
#include "Product.icc"
#undef pyre_grid_Product_icc

#endif

// end of file
