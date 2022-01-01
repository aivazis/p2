# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


# used by the formula compiler
import re
# so I can hold on to my model without making cycles
import weakref


# expressions are strings that describe operations among named nodes
class Expression:
    """
    Support for building evaluation graphs involving nodes that have names registered with a
    {SymbolTable} instance
    """


    # exceptions
    from .exceptions import (
        CircularReferenceError,
        EmptyExpressionError, ExpressionSyntaxError, UnresolvedNodeError,
        EvaluationError )


    # constants
    category = "expression"
    # public data
    expression = None # the expression supplied by the client


    # classifiers
    @property
    def expressions(self):
        """
        Return a sequence over the nodes in my dependency graph that are constructed out of python
        expressions involving the names of other nodes
        """
        # i am one
        yield self
        # nothing further
        return


    # value management
    def getValue(self):
        """
        Compute and return my value
        """
        # attempt
        try:
            # to evaluate my program
            value = eval(self._program, {'model' : self._model })
        # if i run into unresolved nodes
        except self.UnresolvedNodeError:
            # report it
            raise
        # other errors
        except Exception as error:
            # are reported as evaluation errors
            raise self.EvaluationError(node=self, error=error) from None
        # otherwise, just return the value
        return value


    def setValue(self, value):
        """
        Use the new {value} as my formula
        """
        # save the original user input
        self.expression = value
        # interpret {value} as my new formula
        program, operands = self.compile(model=self._model, expression=value)
        # save the referenced nodes as my operands
        self.operands = operands
        # record the evaluator
        self._program = program
        # all done
        return self


    # support for graph traversals
    def identify(self, authority, **kwds):
        """
        Let {authority} know I am an expression
        """
        # invoke the callback
        return authority.onExpression(expression=self, **kwds)


    # meta-methods
    def __init__(self, model, expression, program, **kwds):
        # chain up
        super().__init__(**kwds)
        # build the local state
        self.expression = expression
        self._model = weakref.proxy(model)
        self._program = program
        # all done
        return


    # implementation details
    @classmethod
    def compile(cls, model, expression):
        """
        Compile {expression} and build an evaluator that resolves named references to other
        nodes against {model}.
        """
        # initialize the symbol table
        operands = []
        # define the {re.sub} callback as a local function so it has access to the symbol table
        def handler(match):
            """
            Callback for {re.sub} that extracts node references, adds them to my local symbol
            table and converts them into legal python identifiers
            """
            # if the pattern matched an escaped opening brace
            if match.group("esc_open"):
                # return it as a literal
                return "{"
            # if the pattern matched an escaped closing brace
            if match.group("esc_close"):
                # return it as a literal
                return "}"
            # unmatched braces
            if match.group("lone_open") or match.group("lone_closed"):
                # are errors
                raise cls.ExpressionSyntaxError(
                    expression=expression, error=f"unmatched {match.group()}")
            # only one case left: a valid node reference
            # extract the name from the match
            identifier = match.group('identifier')
            # resolve it
            node = model.resolve(name=identifier)
            # add the node to the operands
            operands.append(node)
            # build and return the matching expression fragment; note the explicit use of
            # {__getitem__} from the {model} to retrieve the actual node value
            return f"(model['{identifier}'])"

        # show me what we start with
        # convert node references to legal python identifiers
        normalized = cls._scanner.sub(handler, expression)
        # show me the normalized expression
        # print(f"  {normalized=}")
        # and the operands
        # print(f"  {operands=}")

        # if there are no symbols, the expression had no node evaluations; but since it may
        # have had escaped braces, make sure the caller has access to the processed value
        if not operands:
            # treat this as an error, for now
            raise cls.EmptyExpressionError(expression=expression, normalized=normalized)

        # now, attempt to compile the expression
        try:
            # by asking python to build a code object
            program = compile(normalized, filename='expression', mode='eval')
        # if it failed
        except SyntaxError as error:
            # complain
            raise cls.ExpressionSyntaxError(expression=expression, error=error) from error
        # all is well
        return program, operands


    @classmethod
    def expand(cls, model, expression):
        """
        Compute the value of {expression} by expanding any references to {model} nodes
        """
        # compile {expression}
        program, _ = cls.compile(model=model, expresion=expresion)
        # evaluate {program} and return the generated value
        return eval(program, {'model': model})


    # private data
    _model = None # my symbol table
    _program = None # the compiled form of my expression
    _scanner = re.compile( # the expression tokenizer
        r"(?P<esc_open>{{)"
        r"|"
        r"(?P<esc_close>}})"
        r"|"
        r"{(?P<identifier>[^}{]+)}"
        r"|"
        r"(?P<lone_open>{)"
        r"|"
        r"(?P<lone_closed>})"
        )


# end of file
