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
jcdev.packages := jcdev.pkg
# libraries
jcdev.libraries := jcdev.lib
# python extensions
jcdev.extensions :=
# and test suites
jcdev.tests := jcdev.lib.tests jcdev.pkg.tests

# the library
# compiler control
jcdev.lib.c++.defines += WHATEVER
jcdev.lib.c++.flags += $($(compiler.c++).std.c++17)
jcdev.lib.c++.libraries := j2

# the package
# meta file
jcdev.pkg.meta :=

# get the testsuites
include jcdev.lib.tests jcdev.pkg.tests

# end of file
