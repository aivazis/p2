# -*- Makefile -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved

# project meta-data
jcdev.major := $(repo.major)
jcdev.minor := $(repo.minor)
jcdev.micro := $(repo.micro)
jcdev.revision := $(repo.revision)

# jcdev builds a python package
jcdev.packages :=
# libraries
jcdev.libraries := jcdev.lib
# python extensions
jcdev.extensions :=
# and test suites
jcdev.tests := jcdev.lib.tests

# compiler control
jcdev.lib.c++.defines += WHATEVER
jcdev.lib.c++.flags += $($(compiler.c++).std.c++17)
jcdev.lib.c++.libraries := j2

# get the testsuites
include jcdev.lib.tests

# end of file
