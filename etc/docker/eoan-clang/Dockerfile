## -*- docker-image-name: "p2:eoan-clang" -*-

# based on ubuntu
FROM ubuntu:eoan

# set up some build variables
# python version
ARG python_version=3.7
ARG python=python${python_version}
# locations
ARG prefix=/usr/local
ARG srcdir=${prefix}/src
# the build system
ARG mm="${python} ${srcdir}/mm/mm.py"

# environment
# colorize (for fun)
ENV TERM=xterm-256color
# set up the dynamic linker path
ENV LD_LIBRARY_PATH=${prefix}/lib
# export the python choice
ENV PYTHON=${python}
# and the path to {mm}
ENV MM=${mm}


# update the package repository
RUN apt update -y
# get the latest
RUN apt dist-upgrade -y

# install the base software stack
#  - {vim} is for interactive use
#  - {openssh}, {zip}, {unzip} are needed for some of the tests
RUN DEBIAN_FRONTEND=noninteractive \
    apt install -y \
        git vim zip unzip \
        openssh-server \
        clang gfortran make \
        ${python} ${python}-dev \
        python3-pybind11 \
        libopenmpi-dev \
        libgsl-dev


# setup the interactive environment
# go home
WORKDIR /root
# copy the files with support for interactive use
COPY etc/docker/eoan-gcc/inputrc .inputrc
# the startup file
COPY etc/docker/eoan-gcc/bashrc bashrc.in
# expand
RUN sed \
        -e "s:@SRCDIR@:${srcdir}:g" \
        bashrc.in > .bashrc

# make the pyre configuration directory
WORKDIR /root/.pyre
# the mpi configuration
COPY etc/docker/eoan-gcc/mpi.pfg mpi.pfg
# the {mm} coniguration file
COPY etc/docker/eoan-clang/mm.pfg mm.pfg.in
# expand
RUN sed \
        -e "s:@PREFIX@:${prefix}:g" \
        mm.pfg.in > mm.pfg

# place the {mm} control file
WORKDIR /root/.mm
# copy the relevant configuration file
COPY etc/docker/eoan-clang/config.mm config.mm.in
# expand
RUN sed \
        -e "s:@PYTHON_VERSION@:${python_version}:g" \
        -e "s:@PYTHON_MODEL@:m:g" \
        config.mm.in > config.mm


# make the development area
WORKDIR ${srcdir}
# pull mm
RUN git clone https://github.com/aivazis/mm.git
# pull p2
COPY . p2

# go to the {p2} top level directory
WORKDIR ${srcdir}/p2
# build
RUN ${mm}
# show me the build context
RUN ${mm} --serial host.info builder.info compilers.info

# start the ssh daemon and test
CMD service ssh start && ${MM} tests


# end of file
