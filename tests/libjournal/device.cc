// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <j2/journal.h>


// alias
using device_t = pyre::journal::device_t;


// the {device} class is abstract, so let's concretize
class Trivial : public device_t {
    // metmethods
public:
    ~Trivial();
    Trivial();

    // interface
public:
    virtual auto memo(verbosity_type, const page_type &, const metadata_type &) -> Trivial &;
    virtual auto alert(verbosity_type, const page_type &, const metadata_type &) -> Trivial &;
};


// metamethods
Trivial::~Trivial() {}
Trivial::Trivial() : device_t("trivial") {}

// the {memo} method
auto Trivial::memo(verbosity_type, const page_type &, const metadata_type &) -> Trivial &
{
    // return myself
    return *this;
}

// and the {alert} method
auto Trivial::alert(verbosity_type, const page_type &, const metadata_type &) -> Trivial &
{
    // return myself
    return *this;
}


// alias the type
using trivial_t = Trivial;


// exercise the trivial device
int main() {
    // instantiate
    trivial_t device;

    // make an entry
    trivial_t::page_type page;
    // and some metadata
    trivial_t::metadata_type metadata;

    // record
    device.memo(1, page, metadata);
    device.alert(1, page, metadata);

    // all done
    return 0;
}


// end of file
