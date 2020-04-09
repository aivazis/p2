# -*- Makefile -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved

# project meta-data
j2.major := $(repo.major)
j2.minor := $(repo.minor)
j2.micro := $(repo.micro)
j2.revision := $(repo.revision)

# j2 builds a python package
j2.packages := j2.pkg
# libraries
j2.libraries := j2.lib
# python extensions
j2.extensions := j2.ext
# and test suites
j2.tests := j2.lib.tests j2.ext.tests

# the j2 library settings
# the file with the library metadata
# j2.lib.meta := meta.cc.in
# the destination include directory
j2.lib.incdir := $(builder.dest.inc)/p2/journal/
# the master header file; it is deposited one level above the rest
j2.lib.master := journal.h
# compiler control
j2.lib.c++.defines += PYRE_CORE
j2.lib.c++.flags += $($(compiler.c++).std.c++17)

# the j2 extension settings
# no need for capsules with {pybind11}?
j2.ext.capsule :=
# the library we are wrapping
j2.ext.wraps := j2.lib
# external dependencies
j2.ext.extern := j2.lib pybind11 python
# compiler control
j2.ext.lib.c++.defines += PYRE_CORE
j2.ext.lib.c++.flags += $($(compiler.c++).std.c++17)

# get the testsuites
include j2.lib.tests j2.ext.tests

# end of file
