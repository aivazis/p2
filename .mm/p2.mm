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
p2.extensions :=
# and test suites
p2.tests := p2.pkg.tests p2.lib.tests

# the p2 package settings
p2.pkg.stem := p2

# get the testsuites
include $(p2.tests)

# end of file
