// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_debuginfo_h)
#define pyre_journal_debuginfo_h


/* the __HERE__ macros */
#include "macros.h"

/* build the declarations of the bindings in a C-compatible way */
#ifdef __cplusplus
extern "C" {
#endif

    bool debuginfo_active(const char * channel);
    void debuginfo_activate(const char * channel);
    void debuginfo_deactivate(const char * channel);
    void debuginfo_out(const char * channel, __HERE_DECL__, const char * fmt, ...);

#ifdef __cplusplus
}
#endif

#endif

// end of file
