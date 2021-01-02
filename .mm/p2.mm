# -*- Makefile -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


# p2 builds a python package
p2.packages := p2.pkg
# libraries
p2.libraries :=
# python extensions
p2.extensions :=
# docker images
p2.docker-images := p2.focal-gcc p2.focal-clang p2.eoan-gcc p2.eoan-clang
# and test suites
p2.tests := p2.pkg.tests


# the docker images
p2.focal-gcc.name := focal-gcc
p2.focal-clang.name := focal-clang
p2.eoan-gcc.name := eoan-gcc
p2.eoan-clang.name := eoan-clang


# the testsuites
include $(p2.tests)

# end of file
