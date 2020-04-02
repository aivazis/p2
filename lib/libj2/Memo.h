// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Memo_h)
#define pyre_journal_Memo_h


// a formatter for messages that are meant for developers, i.e. {debug_t} and {firewall_t}
class pyre::journal::Memo : public Renderer {
    // types
public:

    // metamethods
public:
    virtual ~Memo();
    Memo() = default;

    // implementation details
protected:
    virtual void header(palette_type &, buffer_type &,
                        const entry_type &, const metadata_type &) override;
    virtual void body(palette_type &, buffer_type &,
                      const entry_type &, const metadata_type &) override;

    // disallow
private:
    Memo(const Memo &) = delete;
    Memo(const Memo &&) = delete;
    const Memo & operator= (const Memo &) = delete;
    const Memo & operator= (const Memo &&) = delete;
};


#if 0
// get the inline definitions
#define pyre_journal_Memo_icc
#include "Memo.icc"
#undef pyre_journal_Memo_icc
#endif

#endif

// end of file
