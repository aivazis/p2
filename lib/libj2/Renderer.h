// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_Renderer_h)
#define pyre_journal_Renderer_h


// the interface for formatting diagnostics
class pyre::journal::Renderer {
    // types
public:
    // pointers to me
    using pointer_type = std::shared_ptr<Renderer>;

    using entry_type = page_t;
    using key_type = key_t;
    using value_type = value_t;
    using metadata_type = metadata_t;
    using palette_type = palette_t;

    using bufmsg_type = bufmsg_t;
    using buffer_type = buffer_t;

    // metamethods
public:
    virtual ~Renderer();
    Renderer() = default;

    // interface
public:
    virtual auto render(palette_type &, const entry_type &,
                        const metadata_type &) const -> bufmsg_type;

    // implementation details
protected:
    virtual void header(palette_type &, buffer_type &, const entry_type &,
                        const metadata_type &) const;
    virtual void body(palette_type &, buffer_type &, const entry_type &,
                      const metadata_type &) const;
    virtual void footer(palette_type &, buffer_type &, const entry_type &,
                        const metadata_type &) const;

    // disallow
private:
    Renderer(const Renderer &) = delete;
    Renderer(const Renderer &&) = delete;
    const Renderer & operator= (const Renderer &) = delete;
    const Renderer & operator= (const Renderer &&) = delete;
};


#if 0
// get the inline definitions
#define pyre_journal_Renderer_icc
#include "Renderer.icc"
#undef pyre_journal_Renderer_icc
#endif


#endif

// end of file
