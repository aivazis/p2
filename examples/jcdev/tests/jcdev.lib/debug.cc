// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// standard library
#include <fstream>
// get the journal
#include <p2/journal.h>
// get the custom device support
#include <jcdev/public.h>


// type aliases
using debug_t = pyre::journal::debug_t;
using chronicler_t = pyre::journal::chronicler_t;


// compile time sanity check: make sure the header is accessible
int main(int argc, char * argv[])
{
    // initialize journal; reads command line and environment variables
    pyre::journal::init(argc, argv);

    // add my context to the global metadata
    auto & notes = chronicler_t::notes();
    notes["application"] = "jcdev";

    // create my output stream
    std::ofstream csv("debug.csv");
    // instantiate my custom device
    auto custom = std::make_shared<jcdev::device_t>(csv);
    // install the custom device
    chronicler_t::device(custom);

    // create a channel
    debug_t channel("tests.jcdev.debug");
    // activate it
    channel.activate();
    // say something
    channel
        << pyre::journal::at(__HERE__)
        << "hello world!"
        << pyre::journal::endl;

    // and something else
    channel
        << pyre::journal::at(__HERE__)
        << "this is a longer message" << pyre::journal::newline
        << "that spans a couple of lines"
        << pyre::journal::endl;

    // all done
    return 0;
}


// end of file
