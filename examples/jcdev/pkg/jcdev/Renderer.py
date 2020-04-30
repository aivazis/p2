# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# the csv renderer or
class Renderer:
    """
    Renderer a journal entry as a CSV record
    """


    def render(self, entry):
        """
        Generate the CSV record
        """
        # get the page
        page = entry.page
        # and the notes
        notes = entry.notes

        # the severity
        yield notes["severity"]
        # the registered application name
        yield notes["application"]
        # the channel name
        yield notes["channel"]
        # the filename
        yield notes["filename"]
        # the line number
        yield notes["line"]
        # the function name
        yield notes["function"]

        # and finally, the page contents as a single string
        yield '\n'.join(page)

        # all done
        return


# end of file
