# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


# meta class
from ..patterns.Singleton import Singleton


# declaration
class Dashboard(metaclass=Singleton):
    """
    Singleton that provides access to the pyre executive and its managers
    """

    # grab the base of all pyre exceptions
    from .exceptions import PyreError


    # public data
    @property
    def registrar(self):
        """
        Accessor the component registrar
        """
        # get the registrar
        registrar = self._registrar
        # if we don't have one yet
        if registrar is None:
            # get the factory
            from ..components.Registrar import Registrar
            # make one
            registrar = Registrar()
            # attach it
            self._registrar = registrar
        # all done
        return registrar

    @registrar.setter
    def registrar(self, registrar):
        """
        Attach a new registrar to this dashboard
        """
        # easy enough
        self._registrar = registrar
        # all done
        return


    # metamethods
    def __init__(self, **kwds):
        # chain up
        super().__init__(**kwds)

        # the executive
        self._executive = None

        # framework parts
        self._fileserver = None
        self._nameserver = None
        self._configurator = None

        # infrastructure managers
        self._registrar = None     # the component registrar
        self._schema = None        # the database schema

        # information about the runtime environment
        self._host = None          # the current host
        self._user = None          # the current user
        self._application = None   # the current application

        # all done
        return


    # debugging support
    def dump(self, indent=" "*2, hang=" "*2):
        """
        Dump the status of the dashboard
        """
        # show me
        yield f"{indent}executive: {self._executive}"
        yield f"{indent}{hang}fileserver: {self._fileserver}"
        yield f"{indent}{hang}nameserver: {self._nameserver}"
        yield f"{indent}{hang}configurator: {self._configurator}"
        yield f"{indent}{hang}registrar: {self._registrar}"
        yield f"{indent}{hang}schema: {self._schema}"
        yield f"{indent}{hang}host: {self._host}"
        yield f"{indent}{hang}user: {self._user}"
        yield f"{indent}{hang}application: {self._application}"
        # all done
        return


# end of file
