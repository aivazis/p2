// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// get the journal
#include <p2/journal.h>
// support
#include <cassert>
#include <fstream>
#include <filesystem>


// alias the type
using stream_t = pyre::journal::stream_t;


// exercise the stream device
int main() {
    // the path of the file
    auto filename = std::filesystem::path("file_sanity.out");

    // make a file stream
    auto ofs = std::ofstream(filename);
    // instantiate
    stream_t stream(filename, ofs);
    // check its name
    assert (stream.name() == filename);

    // clean up
    // close the file
    ofs.close();

    // all done
    return 0;
}


// end of file
