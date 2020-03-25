// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_macros_h)
#define pyre_journal_macros_h


// define __HERE__, which has to be a preprocessor macro
// c++20 has <source_location>, so this will soon be obsolete
#if defined(HAVE__FUNC__)

// gcc supports all three
#define __HERE__ __FILE__,__LINE__,__FUNCTION__
// used for the C/FORTRAN bindings
#define __HERE_ARGS__ filename, lineno, funcname
#define __HERE_DECL__ const char * filename, long lineno, const char * funcname

#else

// most compilers have only filename and line number
#define __HERE__ __FILE__,__LINE__
// used for the C/FORTRAN bindings
#define __HERE_ARGS__ filename, lineno
#define __HERE_DECL__ const char * filename, long lineno

#endif // HAVE__FUNC__


#endif

// end of file
