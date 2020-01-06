# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# administrative
def copyright():
    """
    Return the pyre copyright note
    """
    return print(meta.header)


def license():
    """
    Print the pyre license
    """
    # print it
    return print(meta.license)


def version():
    """
    Return the pyre version
    """
    return meta.version


def credits():
    """
    Print the acknowledgments
    """
    # print it
    return print(meta.acknowledgments)


# implementation details
def prerequisites():
    """
    Verify that all prerequisites are satisfied
    """
    # ask the python runtime
    import sys
    # for version information
    major, minor, micro, *_ = sys.version_info
    # currently, the minimum required version is 3.6
    required = (3, 6, 0)
    # so, if this interpreter is older
    if (major, minor, micro) < required:
        # convert the required version into a string
        tag = ".".join(map(str, required))
        # get the correct error report type
        from .framework.exceptions import PyreError
        # make one
        report = PyreError(description=f"pyre requires python {tag} or newer")
        # and complain
        raise report

    # all done
    return


# debugging support
def debug():
    """
    Enable debugging of pyre modules.

    Modules that support debugging must provide a {debug} method and do as little as possible
    during their initialization. The fundamental constraints are imposed by the python import
    mechanism that gives you a single chance to import a module.

    This must be done very early, before pyre itself starts importing its packages. One way to
    request debugging is to create a variable {pyre_debug} in your {__main__} module that
    contains a sequence of strings that are names of pyre modules. This function inspects the
    sequence, imports the corresponding modules, and invokes their {debug} method.
    """
    # get the {__main__} module
    import __main__

    # attempt to
    try:
        # get the list of module names to debug
        names = __main__.pyre_debug
    # if the variable is not set
    except AttributeError:
        # nothing to do, so bail
        return

    # if the user specified {pyre_debug} as a single name
    if isinstance(names, str):
        # convert it to a container
        names = [ names ]

    # get help
    import importlib

    # go through the module names
    for name in names:
        # import each one; use a non-empty {fromList} to ensure we get the submodule itself
        module = importlib.import_module(name)
        # and invoke its debug method
        module.debug()

    # all done
    return


# boot the executive
def boot():
    """
    Bootstrap the framework
    """
    # get the {__main__} module
    import __main__
    # check whether
    try:
        # the user has an opinion on whether to boot the framework
        dashboard = __main__.pyre_dashboard
    # if not
    except AttributeError:
        # grab the dashboard factory
        from .framework.Dashboard import Dashboard
        # and instantiate
        dashboard = Dashboard()
    # if the user had an opinion
    else:
        # that was trivial
        if dashboard is None:
            # no worries; we will handle this case later
            pass
        # if we were not handed a callable
        elif callable(dashboard):
            # invoke it to build the custom dashboard
            dashboard = dashboard()
        # otherwise
        else:
            # get the correct error report type
            from .framework.exceptions import PyreError
            # generate the message
            msg = f"'pyre_dashboard' must be a callable, not '{type(dashboard)}'"
            # make a report
            report = PyreError(description=msg)
            # and complain
            raise report

        # now for some dirty work: get the singleton factory
        from .framework.Dashboard import Dashboard
        # and install the new dashboard as the singleton so users can access it either through
        # the global variable in this package or the usual way through the singleton
        Dashboard.pyre_singletonInstance = dashboard

    # if we are supposed to boot
    if dashboard is not None:
        # do whatever it takes to get the framework to boot
        pass

    # and return it
    return dashboard


# kick start
prerequisites()
# first, invoke the {debug} method in case the user asked for debugging support
debug()
# boot
dashboard = boot()
# if successful
if dashboard is not None:
    # publish
    from . import meta


# end of file
