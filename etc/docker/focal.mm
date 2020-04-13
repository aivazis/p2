# -*- Makefile -*-
#
# michael a.g. aïvázis
# parasim
# (c) 1998-2020 all rights reserved
#

# system tools
sys.prefix := /usr
# the users' install directory
user.prefix := $(HOME)/tools

# gsl
gsl.version := 2.5
gsl.dir := $(sys.prefix)

# numpy
numpy.version := 1.17.4
numpy.dir := $(sys.prefix)/lib/python3/dist-packages/numpy/core

# pybind11
pybind11.version := 2.3.0
pybind11.dir = $(sys.prefix)

# python
python.version := @PYTHON_VERSION@
python.dir := $(sys.prefix)
python.incdir := $(python.dir)/include/python$(python.version)
python.libdir := $(python.dir)/lib/python$(python.version)
# set the compiler so we don't depend on the symbolic link, which may not even be there
compiler.python := python$(python.version)

# end of file
