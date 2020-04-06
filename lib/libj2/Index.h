// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Index_h)
#define pyre_journal_Index_h


// owner of the map (channel name -> shared channel state)
// each concrete subclass of {diagnostic} maintains its own index as class data, shared among
// its instances
template <typename inventoryT>
class pyre::journal::Index {
    // types
public:
    using name_type = name_t;
    using inventory_type = inventoryT;
    using index_type = std::map<name_type, inventory_type>;

    // metamethods
public:
    inline Index() = default;
    inline Index(const Index &) = default;
    inline Index(Index &&) = default;
    inline Index & operator= (const Index &) = default;
    inline Index & operator= (Index &&) = default;

    // interface
public:
    // simple access to the underlying index
    inline auto size() const;
    inline auto empty() const;
    inline auto contains(const name_type &) const -> bool;

    // iteration
    inline auto begin() const;
    inline auto end() const;

    // channel look up
    inline auto lookup(const name_type &) -> inventory_type &;
    // manual inventory placement
    inline void insert(const name_type &, const inventory_type &);

    // data members
private:
    index_type _index;

    // disallow
private:
};


// get the inline definitions
#define pyre_journal_Index_icc
#include "Index.icc"
#undef pyre_journal_Index_icc


#endif

// end of file
