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
    using string_type = std::string;
    using name_type = string_type;
    using inventory_type = inventoryT;
    using index_type = std::map<name_type, inventory_type>;

    // metamethods
public:
    inline Index();

    // interface
public:
    inline auto lookup(const name_type &) -> inventory_type &;

    inline auto size() const;
    inline auto empty() const;

    inline auto begin() const;
    inline auto end() const;

    // data members
private:
    index_type _index;

    // disallow
private:
    Index(const Index &) = delete;
    Index(const Index &&) = delete;
    const Index & operator= (const Index &) = delete;
    const Index & operator= (const Index &&) = delete;
};


// get the inline definitions
#define pyre_journal_Index_icc
#include "Index.icc"
#undef pyre_journal_Index_icc


#endif

// end of file
