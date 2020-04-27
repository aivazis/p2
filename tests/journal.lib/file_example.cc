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
using debug_t = pyre::journal::debug_t;
using stream_t = pyre::journal::stream_t;


// exercise the stream device
int main() {
    // the path of the file
    auto filename = std::filesystem::path("file_example.out");
    // make a file stream
    auto ofs = std::ofstream(filename);

    // make a channel
    debug_t channel("test.journal.file");
    // set its device
    channel.device(std::make_shared<stream_t>(filename, ofs));
    // activate
    channel.activate();

    // inject something
    channel
        << pyre::journal::at(__HERE__)
        << "hello world!"
        << pyre::journal::endl;

    // all done
    return 0;
}


// end of file
