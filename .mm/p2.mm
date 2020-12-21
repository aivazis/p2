# -*- Makefile -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# p2 builds a python package
p2.packages := p2.pkg
# libraries
p2.libraries :=
# python extensions
p2.extensions := p2.ext
# docker images
p2.docker-images := p2.focal-gcc p2.focal-clang p2.eoan-gcc p2.eoan-clang
# and test suites
p2.tests := p2.pkg.tests p2.ext.tests


# the p2 extension settings
# no cpsules to export with {pybind11}
p2.ext.capsule :=
# wrap the pyre library
p2.ext.wraps := p2.lib
# dependencies to other project parts
p2.ext.prerequisites :=  p2.pkg p2.lib
# external dependencies
p2.ext.extern := p2.lib pyre pybind11 python
# compiler control
p2.ext.lib.c++.defines += PYRE_CORE
p2.ext.lib.c++.flags += $($(compiler.c++).std.c++17)


# the docker images
p2.focal-gcc.name := focal-gcc
p2.focal-clang.name := focal-clang
p2.eoan-gcc.name := eoan-gcc
p2.eoan-clang.name := eoan-clang


# the testsuites
include $(p2.tests)

# end of file
