// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <j2/journal.h>


// the {device} class is abstract, so let's concretize
class Trivial : public pyre::journal::device_t {
    // metmethods
public:
    ~Trivial();

    // interface
public:
    virtual auto record(const entry_type &, const metadata_type &) -> Trivial &;
};


// implement the destructor
Trivial::~Trivial() {}

// and the {record} method
auto Trivial::record(const entry_type &, const metadata_type &) -> Trivial &
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
    trivial_t::entry_type entry;
    // and some metadata
    trivial_t::metadata_type metadata;

    // record
    device.record(entry, metadata);

    // all done
    return 0;
}


// end of file
