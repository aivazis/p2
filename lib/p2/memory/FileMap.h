// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_memory_FileMap_h)
#define pyre_memory_FileMap_h


// a file-backed memory map

// use cases:

// - read only existing product
//   need: filename
//   edge cases: fail if file doesn't exist

// - read/write existing product
//   need: filename
//   edge cases:

// - create data product
//   need: filename, size in bytes
//   edge cases: what to do if file already exists


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
    // flags
    using writable_type = bool;
    using clobber_type = bool;

    // metamethods
public:
    // destructor
    inline ~FileMap();

    // constructors
    // map an existing data product given its filename
    inline explicit FileMap(uri_type, writable_type = false);
    // create a new product of a given size in bytes
    inline FileMap(uri_type, size_type);

    // interface
public:
    inline auto bytes() const;
    inline auto writable() const;
    inline auto data() const;

    // syntactic sugar
    inline operator pointer () const;

    // implementation details: methods
private:
    void stat();
    void create();
    void map();
    void unmap();

    // implementation details: data
private:
    uri_type _uri;
    info_type _info;
    size_type _bytes;
    pointer _data;
    writable_type _writable;

    // disallow
private:
    FileMap(const FileMap &) = delete;
    FileMap(const FileMap &&) = delete;
    const FileMap & operator= (const FileMap &) = delete;
    const FileMap & operator= (const FileMap &&) = delete;
};


// get the inline definitions
#define pyre_memory_FileMap_icc
#include "FileMap.icc"
#undef pyre_memory_FileMap_icc


#endif

// end of file
