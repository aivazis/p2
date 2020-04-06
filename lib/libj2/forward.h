// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_forward_h)
#define pyre_journal_forward_h


// forward declarations of all user facing entities
namespace pyre::journal {
    // the exceptions
    class firewall_error;

    // terminal support
    class ASCII;
    class CSI;
    class ANSI;

    // devices
    class Device;
    class Trash;
    class Stream;
    class Console;
    class ErrorConsole;

    // renderers
    class Renderer;
    class Memo;
    class Alert;

    // the channel stream manipulators; some are actual class, others are functions that take
    // and return a channel
    // verbosity level
    class Verbosity;
    // location information
    class Locator;
    // metadata manipulation
    class Selector;

    // the null diagnostic; used when channels are turned off at compile time
    class Null;
    // end of transaction
    inline auto endl(const Null &) -> const Null &;
    // mark the end of a line of output
    inline auto newline(const Null &) -> const Null &;
    // injection operators
    // verbosity level
    inline auto
    operator<< (const Null &, const Verbosity &) -> const Null &;
    // location info
    inline auto
    operator<< (const Null &, const Locator &) -> const Null &;
    // metadata
    inline auto
    operator<< (const Null &, const Selector &) -> const Null &;
    // injection of a manipulator function
    inline auto
    operator<< (const Null &, const Null & (*)(const Null &)) -> const Null &;
    // injection of everything else
    template <typename itemT>
    inline auto
    operator<< (const Null &, const itemT &) -> const Null &;

    // the singleton with the global journal settings
    class Chronicler;
    // the common channel state
    template <bool = true> class Inventory;
    // firewall state
    class FirewallInventory;
    // storage/retrieval for common channel state
    template <typename> class Index;
    // live channels are implemented using two different base classes:
    // the controller of the channel state
    template <typename severityT, typename inventoryT> class Channel;
    // the recorder of the channel message
    template <typename severityT> class Diagnostic;
    // the built-in channels
    class Debug;
    class Firewall;
    class Informational;
    class Warning;
    class Error;
    // end of transaction
    template <typename severityT>
    inline auto endl(Diagnostic<severityT> &) -> Diagnostic<severityT> &;
    // end of a line of output
    template <typename severityT>
    inline auto newline(Diagnostic<severityT> &) -> Diagnostic<severityT> &;
    // injection operators
    // verbosity info
    template <typename severityT>
    inline auto
    operator<< (Diagnostic<severityT> &, const Verbosity &) -> Diagnostic<severityT> &;
    // location info
    template <typename severityT>
    inline auto
    operator<< (Diagnostic<severityT> &, const Locator &) -> Diagnostic<severityT> &;
    // metadata
    template <typename severityT>
    inline auto
    operator<< (Diagnostic<severityT> &, const Selector &) -> Diagnostic<severityT> &;
    // injection of manipulator functions
    template <typename severityT>
    inline auto
    operator<< (Diagnostic<severityT> &,
                Diagnostic<severityT> & (*)(Diagnostic<severityT> &))
        -> Diagnostic<severityT> &;
    // injection of everything else
    template <typename severityT, typename itemT>
    inline auto operator<< (Diagnostic<severityT> &, const itemT &) -> Diagnostic<severityT> &;
}


// low level api
#if defined(PYRE_CORE)
namespace pyre::journal {
    // infrastructure
    template <typename inventoryT>
    using index_t = Index<inventoryT>;

    template <bool stateV = true>
    using inventory_t = Inventory<stateV>;

    using firewallInventory_t = FirewallInventory;

    template <typename severityT, typename inventoryT>
    using channel_t = Channel<severityT, inventoryT>;

    template <typename severityT>
    using diagnostic_t = Diagnostic<severityT>;

    using chronicler_t = Chronicler;

    using memo_t = Memo;
    using alert_t = Alert;
}
#endif


// developer api
namespace pyre::journal {
    // the null diagnostic is always available
    using null_t = Null;

    // if we are building the library
#if defined(PYRE_CORE)
    // enable the developer channels
    using debug_t = Debug;
    using firewall_t = Firewall;

    // if the user has explicitly requested no debugging
#elif defined(NDEBUG)
    // disable the developer channels
    using debug_t = null_t;
    using firewall_t =  null_t;

    // if the user has explicitly asked for debugging support
#elif defined(DEBUG) || defined(JOURNAL_DEBUG)
    // enable the developer channels
    using debug_t = Debug;
    using firewall_t = Firewall;

    // otherwise, assume this is a production build
#else
    // disable the developer channels
    using debug_t =  null_t;
    using firewall_t =  null_t;
#endif
}


// user facing api
namespace pyre::journal {
    // infrastructure
    // terminal support
    using ascii_t = ASCII;
    using csi_t = CSI;
    using ansi_t = ANSI;

    // devices
    using device_t = Device;
    using trash_t = Trash;
    using stream_t = Stream;
    using cout_t = Console;
    using cerr_t = ErrorConsole;

    // channels
    using error_t = Error;
    using info_t = Informational;
    using warning_t = Warning;

    // manipulators
    using at = Locator;
    using set = Selector;
    using verbosity = Verbosity;

    // convenience
    inline void init(int argc, char* argv[]);
}


#endif

// end of file
