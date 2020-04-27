// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2020 all rights reserved

// code guard
#if !defined(pyre_journal_manipulators_h)
#define pyre_journal_manipulators_h


// manipulators
// end of transaction
template <typename severityT, template <class> typename proxyT>
auto
pyre::journal::
endl(Channel<severityT, proxyT> & channel) -> Channel<severityT, proxyT> &
{
    // ask the channel to record the accumulated message
    return channel.log();
}


template <typename severityT, template <class> typename proxyT>
auto
pyre::journal::
newline(Channel<severityT, proxyT> & channel) -> Channel<severityT, proxyT> &
{
    // ask the channel entry to mark the end of a line of output
    return channel.line();
}


// the injection operators
// verbosity level
template <typename severityT, template <class> typename proxyT>
auto
pyre::journal::
operator<< (Channel<severityT, proxyT> & channel, const Verbosity & verbosity)
    -> Channel<severityT, proxyT> &
{
    // adjust the verbosity of the channel
    channel.verbosity(verbosity.verbosity());
    // all done
    return channel;
}


// location info
template <typename severityT, template <class> typename proxyT>
auto
pyre::journal::
operator<< (Channel<severityT, proxyT> & channel, const Locator & locator)
    -> Channel<severityT, proxyT> &
{
    // use the locator information to set channel entry metadata
    channel.entry().note("filename", locator.file());
    channel.entry().note("line", locator.line());
    channel.entry().note("function", locator.func());

    // all done
    return channel;
}


// metadata
template <typename severityT, template <class> typename proxyT>
auto
pyre::journal::
operator<< (Channel<severityT, proxyT> & channel, const Note & note)
    -> Channel<severityT, proxyT> &
{
    // transfer the note to the current entry
    channel.entry().note(note.key(), note.value());
    // all done
    return channel;
}


// injection of manipulator functions
template <typename severityT, template <class> typename proxyT>
inline auto
pyre::journal::
operator<< (Channel<severityT, proxyT> & channel,
            Channel<severityT, proxyT> & (*manipulator)(Channel<severityT, proxyT> &))
    -> Channel<severityT, proxyT> &
{
    // invoke the manipulator function with the {channel} as an argument
    return manipulator(channel);
}


// injection of everything else
template <typename itemT, typename severityT, template <class> typename proxyT>
auto
pyre::journal::
operator<< (Channel<severityT, proxyT> & channel, const itemT & item)
    -> Channel<severityT,proxyT> &
{
    // inject the item in the channel and return the channel
    channel.entry().inject(item);
    // enable chaining
    return channel;
}


#endif

// end of file
