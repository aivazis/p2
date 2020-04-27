// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_api_h)
#define pyre_journal_api_h


// end user facing api
namespace pyre::journal {
    // the initializer of the global settings
    inline void init(int argc, char* argv[]);

    // channels
    using info_t = Informational;
    using warning_t = Warning;
    using error_t = Error;

    // the keeper of the global settings
    using chronicler_t = Chronicler;

    // devices
    using trash_t = Trash;
    using stream_t = Stream;
    using cout_t = Console;
    using cerr_t = ErrorConsole;


    // manipulators
    using at = Locator;
    using note = Note;
    using verbosity = Verbosity;
}


// the developer facing api
namespace pyre::journal {
    // null diagnostic: always available
    using null_t = Null;

    // if we are building the library
#if defined(PYRE_CORE)
    // enable the developer channels
    using debug_t = Debug<InventoryProxy>;
    using firewall_t = Firewall;

    // if the user has suppressed debugging support explicitly
#elif defined(NDEBUG)
    // disable the developer channels
    using debug_t = null_t;
    using firewall_t = null_t;

    // if the user has requested debugging support explicitly
#elif defined(DEBUG) || defined(JOURNAL_DEBUG)
    // enable the developer channels
    using debug_t = Debug;
    using firewall_t = Firewall;

    // otherwise, this is a production build
#else
    // disable the developer channels
    using debug_t =  null_t;
    using firewall_t = null_t;
#endif
}


// low level api; chances are good you shouldn't access these directly
namespace pyre::journal {
    // message entry
    using entry_t = Entry;

    // shared channel state
    using inventory_t = Inventory;

    template <class clientT>
    using inventory_proxy_t = InventoryProxy<clientT>;

    template <class severityT, template <typename> class proxyT = inventory_proxy_t>
    using channel_t = Channel<severityT, proxyT>;

    using index_t = Index;

    // renderers
    using renderer_t = Renderer;
    using renderer_ptr = std::shared_ptr<renderer_t>;
    using memo_t = Memo;
    using alert_t = Alert;

    // devices
    using device_t = Device;
    using device_ptr = std::shared_ptr<Device>;

    // aliases for the manipulators
    using locator_t = Locator;
    using note_t = Note;

    // terminal support
    using ascii_t = ASCII;
    using csi_t = CSI;
    using ansi_t = ANSI;
}


#endif

// end of file