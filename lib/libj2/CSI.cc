// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// for the build system
#include <portinfo>
// get the forward declarations
#include "forward.h"
// external support
#include "externals.h"
// get the support we need
#include "ASCII.h"
#include "CSI.h"


// initialize {esc}
const pyre::journal::CSI::rep_type
pyre::journal::CSI::esc(1, ASCII::ESC);


// end of file
