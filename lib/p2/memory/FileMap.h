// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_memory_FileMap_h)
#define pyre_memory_FileMap_h


// a file-backed memory map
class pyre::memory::FileMap {
    // types
public:
    // the address of the mapping
    using pointer = void *;
    // file paths
    using uri_type = uri_t;
    // file information
    using info_type = info_t;
    // sizes and offsets
    using size_type = size_t;
    using offset_type = offset_t;
    // flags
    using writable_type = bool;
    using preserve_type = bool;

    // metamethods
public:
    // destructor
    ~FileMap();
    // constructor
    FileMap(uri_type, writable_type, size_type, offset_type, preserve_type);

    // implementation details: data
private:
    uri_type _uri;
    info_type _info;
    size_type _bytes;
    pointer _buffer;

    // disallow
private:
    FileMap(const FileMap &) = delete;
    FileMap(const FileMap &&) = delete;
    const FileMap & operator= (const FileMap &) = delete;
    const FileMap & operator= (const FileMap &&) = delete;
};


#endif

// end of file
