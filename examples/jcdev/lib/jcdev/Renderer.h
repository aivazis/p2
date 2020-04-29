// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(jcdev_Renderer_h)
#define jcdev_Renderer_h


// custom renderer
class jcdev::Renderer {
    // types
public:
    // pointers to me
    using pointer_type = std::shared_ptr<Renderer>;

    using page_type = pyre::journal::page_t;
    using key_type = pyre::journal::key_t;
    using value_type = pyre::journal::value_t;
    using metadata_type = pyre::journal::metadata_t;

    using record_type = record_t;

    // metamethods
public:
    Renderer();
    virtual ~Renderer();

    // interface
public:
    virtual auto render(const page_type &, const metadata_type &) const -> record_type;

    // implementation details
private:

    // disallow
private:
    Renderer(const Renderer &) = delete;
    Renderer(const Renderer &&) = delete;
    const Renderer & operator= (const Renderer &) = delete;
    const Renderer & operator= (const Renderer &&) = delete;
};


#endif

// end of file
