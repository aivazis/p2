// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_grid_Rep_h)
#define pyre_grid_Rep_h


// thin adaptor over a compile time container that we use to store index ranks, grid shapes,
// packing order and the like; it provides an abstraction layer that is necessary for
// supporting the implementation in environments that don't have {std::array}
template <class containerT>
class pyre::grid::Rep {
    // types
public:
    // alias for me
    using rep_type = Rep<containerT>;
    // and my container
    using container_type = containerT;
    // sizes of things
    using size_type = typename containerT::size_type;
    // my value
    using value_type = typename container_type::value_type;
    using pointer = typename container_type::pointer;
    using const_pointer = typename container_type::const_pointer;
    using reference = typename container_type::reference;
    using const_reference = typename container_type::const_reference;
    // offsets
    using difference_type = typename container_type::difference_type;
    // container access
    using iterator = typename container_type::iterator;
    using const_iterator = typename container_type::const_iterator;
    using reverse_iterator = typename container_type::reverse_iterator;
    using const_reverse_iterator = typename container_type::const_reverse_iterator;

    // metamethods
public:
    // aggregate initialization
    template <typename... argT>
    constexpr explicit Rep(argT...);

    // access
public:
    // bounds checked
    constexpr auto at(size_type) -> reference;
    constexpr auto at(size_type) const -> const_reference;

    // random access
    constexpr auto operator[](size_type) -> reference;
    constexpr auto operator[](size_type) const -> const_reference;

    // fill with a specific value
    constexpr void fill(const_reference);

    // iteration
public:
    // forward
    constexpr auto begin() -> iterator;
    constexpr auto begin() const -> const_iterator;
    constexpr auto end() -> iterator;
    constexpr auto end() const -> const_iterator;
    // reverse
    constexpr auto rbegin() -> reverse_iterator;
    constexpr auto rbegin() const -> const_reverse_iterator;
    constexpr auto rend() -> reverse_iterator;
    constexpr auto rend() const -> const_reverse_iterator;
    // const
    constexpr auto cbegin() const -> const_iterator;
    constexpr auto cend() const -> const_iterator;
    constexpr auto crbegin() const -> const_reverse_iterator;
    constexpr auto crend() const -> const_reverse_iterator;

    // static interface
public:
    static constexpr auto rank() -> size_type;
    static constexpr auto zero() -> rep_type;

    // default metamethods
public:
    // destructor
    ~Rep() = default;
    // constructors
    Rep(const Rep &) = default;
    Rep(Rep &&) = default;
    Rep & operator=(const Rep &) = default;
    Rep & operator=(Rep &&) = default;

    // implementation details: data
private:
    container_type _rep;
};


// get the inline definitions
#define pyre_grid_Rep_icc
#include "Rep.icc"
#undef pyre_grid_Rep_icc


#endif

// end of file
