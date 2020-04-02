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
    using string_type = Device::string_type;

    using entry_type = Device::entry_type;
    using key_type = Device::key_type;
    using value_type = Device::value_type;
    using metadata_type = Device::metadata_type;
    using palette_type = Device::palette_type;

    using buffer_type = std::stringstream;

    // metamethods
public:
    virtual ~Renderer();
    Renderer() = default;

    // interface
public:
    virtual auto render(palette_type &, const entry_type &, const metadata_type &) -> string_type;

    // implementation details
protected:
    virtual void header(palette_type &, buffer_type &, const entry_type &, const metadata_type &);
    virtual void body(palette_type &, buffer_type &, const entry_type &, const metadata_type &);
    virtual void footer(palette_type &, buffer_type &, const entry_type &, const metadata_type &);

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
