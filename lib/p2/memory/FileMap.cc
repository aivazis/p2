// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved


// externals
#include "externals.h"
// forward declarations
#include "forward.h"
// type aliases
#include "api.h"

// my class declaration
#include "FileMap.h"


pyre::memory::FileMap::
FileMap(uri_type uri, writable_type writable) :
    _uri { uri },
    _info {},
    _bytes {},
    _buffer { nullptr },
    _writable { writable }
{
    // make a channel
    pyre::journal::debug_t channel("pyre.memory.map");
    // sign on
    channel
        << "mapping existing data product:" << pyre::journal::newline
        << "  name: '" << _uri << "'"
        << "  size: '" << _bytes << " bytes"
        << pyre::journal::endl(__HERE__);

    // all done
    return;
}


pyre::memory::FileMap::
FileMap(uri_type uri, size_type bytes) :
    _uri { uri },
    _info {},
    _bytes { bytes },
    _buffer { nullptr },
    _writable { true }
{
    // make a channel
    journal::debug_t channel("pyre.memory.map");
    // sign on
    channel
        << "creating a new data product:" << pyre::journal::newline
        << "  name: '" << _uri << "'" << pyre::journal::newline
        << "  size: " << _bytes << " bytes"
        << pyre::journal::endl(__HERE__);

    // all done
    return;
}


// implementation details
// open the backing for an existing data product given its name
void
pyre::memory::FileMap::
stat()
{
    // pull an old fashioned string out of the pathname
    auto filename = _uri.c_str();
    // find out what the filesystem knows about this file
    auto status = ::stat(filename, &_info);
    // if something went wrong
    if (status) {
        // make a channel
        pyre::journal::error_t channel("pyre.memory.map");
        // complain
        channel
            << "while opening '" << _uri << "':" << pyre::journal::newline
            << "stat: error " << errno << ": " << std::strerror(errno)
            << pyre::journal::endl(__HERE__);
    }

    // get the file size
    _bytes = _info.st_size;

    // all done
    return;
}


// create the backing file for a new data product given its name and size
void
pyre::memory::FileMap::
create()
{
    // we take advantage of the POSIX requirement that writing past the end of a file
    // automatically fills all preceding locations with nulls
    // make a stream
    std::ofstream f(_uri, std::ofstream::binary);
    // move the file pointer to the desired location
    f.seekp(_bytes - 1);
    // make a byte
    char null = 0;
    // place it into the file
    f.write(&null, sizeof(null));
    // close the stream
    f.close();
    // all done
    return;
}


// create a file backed memory map, given the name and size of the file
void
pyre::memory::FileMap::
map()
{
    // deduce the access mode
    auto mode = _writable ? O_RDWR : O_RDONLY;
    // open the file using the low level IO routine; we need its file descriptor
    auto fd = ::open(_uri.c_str(), mode);
    // if something went wrong
    if (fd < 0) {
        // make a channel
        pyre::journal::error_t channel("pyre.memory.map");
        // complain
        channel
            << "while mapping '" << _uri << "':" << pyre::journal::newline
            << "open: error " << errno << ": " << std::strerror(errno)
            << pyre::journal::endl(__HERE__);
        // unreachable, unless the user has marked this error as non-fatal
        return;
    }

    // derive the protection flag for the mapping
    auto protection = _writable ? (PROT_READ | PROT_WRITE) : PROT_READ;
    // map it
    _buffer = ::mmap(nullptr, _bytes, protection, MAP_SHARED, fd, 0);
    // if something went wrong
    if (_buffer == MAP_FAILED) {
        // make a channel
        pyre::journal::error_t channel("pyre.memory.map");
        // complain
        channel
            << "while mapping '" << _uri << "':" << pyre::journal::newline
            << "map: error " << errno << ": " << std::strerror(errno)
            << pyre::journal::endl(__HERE__);
        // unreachable, unless the user has marked this error as non-fatal
        return;
    }

    // make a channel
    pyre::journal::debug_t channel("pyre.memory.map");
    // and report success
    channel
        << "'" << _uri << "':" << pyre::journal::newline
        << "mapped " << _bytes << " bytes of "
        << (_writable ? "read/write" : "read only") << " memory at " << _buffer
        << pyre::journal::endl(__HERE__);

    // close the file descriptor; we don't need it any more
    ::close(fd);

    // all done
    return;
}


// unmap file backed memory
void
pyre::memory::FileMap::
unmap()
{
    // if we don't have a valid map
    if (_buffer == MAP_FAILED || _bytes == 0) {
        // nothing to do
        return;
    }

    // otherwise, unmap
    auto status = ::munmap(_buffer, _bytes);
    // if something went wrong
    if (status) {
        // make a channel
        pyre::journal::warning_t channel("pyre.memory.map");
        // complain
        channel
            << "while unmapping '" << _uri << "':" << pyre::journal::newline
            << "munmap: error " << errno << ": " << std::strerror(errno)
            << pyre::journal::endl(__HERE__);
    }

    // all done
    return;
}



// end of file
