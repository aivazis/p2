// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Entry_h)
#define pyre_journal_Entry_h


// encapsulation of a journal message entry
class pyre::journal::Entry
{
    // types
public:
    // message payload
    using page_type = page_t;
    // message metadata
    using key_type = key_t;
    using value_type = value_t;
    using notes_type = notes_t;
    // message buffering
    using line_type = line_t;
    using linebuf_type = linebuf_t;
    // output streams
    using ostream_type = outputstream_t;

    // metamethods
public:
    // constructors
    inline explicit Entry();

    // interface
public:
    // accessors
    inline auto buffer() -> linebuf_type &;
    inline auto page() const -> const page_type &;
    inline auto notes() const -> const notes_type &;

    // transaction support
public:
    inline auto note(const key_type &, const value_type &) -> Entry &;
    // move the buffer to the page and reset
    inline auto push() -> Entry &;
    // clear the page
    inline auto flush() -> Entry &;

    // item injection
    template <typename itemT>
    inline void inject(const itemT &);

    // data
private:
    linebuf_type _buffer;
    page_type _page;
    notes_type _notes;

    // disallow
private:
    Entry(const Entry &) = delete;
    Entry(Entry &&) = delete;
    Entry & operator= (const Entry &) = delete;
    Entry & operator= (Entry &&) = delete;
};


// get the inline definitions
#define pyre_journal_Entry_icc
#include "Entry.icc"
#undef pyre_journal_Entry_icc


#endif

// end of file
