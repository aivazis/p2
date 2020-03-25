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
j2.packages :=
# libraries
j2.libraries := j2.lib
# python extensions
j2.extensions :=
# and test suites
j2.tests := j2.lib.tests

# the j2 library settings
j2.lib.stem := j2
j2.lib.c++.defines += PYRE_CORE
j2.lib.c++.flags += $($(compiler.c++).std.c++17)

# get the testsuites
include j2.tests

# end of file
