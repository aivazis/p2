// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Trash_h)
#define pyre_journal_Trash_h


// a device that ignores all requests for output
class pyre::journal::Trash : public Device {
    // types
public:
    // pointers to me
    using pointer_type = std::shared_ptr<Trash>;

    using palette_type = palette_t;
    using renderer_type = Renderer;
    using renderer_pointer = Renderer::pointer_type;

    // metamethods
public:
    // constructor
    inline Trash();
    // destructor
    virtual ~Trash();

    // interface
public:
    // developer diagnostics
    virtual auto memo(verbosity_type, const page_type &, const metadata_type &) -> Trash &;
    // user facing diagnostics
    virtual auto alert(verbosity_type, const page_type &, const metadata_type &) -> Trash &;

    // data
private:
    // the renderer for memos
    renderer_pointer _memo;
    // the renderer for alerts
    renderer_pointer _alert;

    // disallow
private:
    Trash(const Trash &) = delete;
    Trash(const Trash &&) = delete;
    const Trash & operator= (const Trash &) = delete;
    const Trash & operator= (const Trash &&) = delete;
};


// get the inline definitions
#define pyre_journal_Trash_icc
#include "Trash.icc"
#undef pyre_journal_Trash_icc


#endif

// end of file
