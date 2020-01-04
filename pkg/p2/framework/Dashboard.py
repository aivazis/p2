# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# declaration
class Dashboard:
    """
    Mix-in class that provides access to the pyre executive and its managers
    """

    # grab the base of all pyre exceptions
    from .exceptions import PyreError


    # public data
    # the executive
    pyre_executive = None

    # framework parts
    pyre_fileserver = None
    pyre_nameserver = None
    pyre_configurator = None

    # infrastructure managers
    pyre_registrar = None # the component registrar
    pyre_schema = None # the database schema

    # information about the runtime environment
    pyre_host = None # the current host
    pyre_user = None # the current user
    pyre_application = None # the current application


    # debugging support
    @classmethod
    def dashboard(cls):
        """
        Dump the status of the dashboard
        """
        # show me
        yield f"executive: {cls.pyre_executive}"
        yield f"  fileserver: {cls.pyre_fileserver}"
        yield f"  nameserver: {cls.pyre_nameserver}"
        yield f"  configurator: {cls.pyre_configurator}"
        yield f"  registrar: {cls.pyre_registrar}"
        yield f"  schema: {cls.pyre_schema}"
        yield f"  host: {cls.pyre_host}"
        yield f"  user: {cls.pyre_user}"
        yield f"  application: {cls.pyre_application}"
        # all done
        return


# end of file
