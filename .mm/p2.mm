# -*- Makefile -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved

# project meta-data
p2.major := $(repo.major)
p2.minor := $(repo.minor)
p2.micro := $(repo.micro)
p2.revision := $(repo.revision)

# p2 builds a python package
p2.packages := p2.pkg
# libraries
p2.libraries := p2.lib
# python extensions
p2.extensions := p2.ext
# and test suites
p2.tests := p2.pkg.tests p2.lib.tests p2.ext.tests


# the p2 library settings
p2.lib.c++.defines += PYRE_CORE
p2.lib.c++.flags += $($(compiler.c++).std.c++17)


# the p2 extension settings
# no cpsules to export with {pybind11}
p2.ext.capsule :=
# wrap the pyre library
p2.ext.wraps := p2.lib
# dependencies to other project parts
p2.ext.prerequisites :=  p2.pkg j2.lib p2.lib
# external dependencies
p2.ext.extern := p2.lib j2.lib pybind11 python
# compiler control
p2.ext.lib.c++.defines += PYRE_CORE
p2.ext.lib.c++.flags += $($(compiler.c++).std.c++17)


# get the testsuites
include $(p2.tests)

# end of file
