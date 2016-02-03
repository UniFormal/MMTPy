from MMTPy.bridge import bridge
from MMTPy.content.objects.terms import term
from MMTPy.library.lf import wrappers

class Term(bridge.Bridge):
    """
    An Term() object represents a Bridge() that wraps an MMT Object.
    """

    def __init__(self, qclient, tm, previous = None):
        """
        Creates a new Term() object for MMT. Note that this function should
        never be called manually but always automatically through another
        Bridge() method.

        Arguments:

        qclient
            A QMTClient object representing the connection to MMT.
        tm
            A Term containing the actual declaration
        previous
            A previous Bridge object (if applicable)
        """

        super(Term, self).__init__(qclient, previous = previous)

        if isinstance(tm, term.Term):
            self.__tm = tm
        else:
            raise TypeError("tm parameter must be an Term()")

        from MMTPy.bridge import declaration
        if isinstance(previous, declaration.Declaration):
            self.__gn = previous.toPath()
        else:
            self.__gn = None

    def __eq__(self, other):
        return isinstance(other, Term) and other.__tm == self.__tm

    def parent(self):
        """
        Gets the Declaration() matching this Term().
        """

        if self.__gn == None:
            raise bridge.NoParentException()

        return bridge.Bridge.create(self, self.__gn)

    def getDeclaration(self):
        """
        Gets the Declaration() matching this Term()
        """

        return self.parent()

    def getModule(self):
        """
        Gets the Module() matching this Term()
        """
        return self.getDeclaration().getModule()

    def getNamespace(self):
        """
        Gets the Namespace() matching this Term()
        """

        return self.getDeclaration().getModule().getNamespace()

    def get(self):
        """
        Gets the underlying term that is wrapped by this Term().
        """

        return self.__tm

    def toPath(self):
        """
        Turns this Term() object into a matching Path() object
        """
        return self.__gn

    def navigate(self, pth):
        """
        Navigates this bridge to a given path. Not applicable.
        """

        raise NotImplementedError

    #
    # LF Function Types
    #
    def asFunctionType(self):
        """
        Assumes this term represents an LF function type and returns a triple
        (variables, argument_types, return_type)
        """

        (v, a, r) = wrappers.lf_unpack_function_types(self.get())

        return ([bridge.Bridge.create(self, vv) for vv in v], [bridge.Bridge.create(self, aa) for aa in a], bridge.Bridge.create(self, r))


    def getArgumentTypes(self):
        """
        Assumes this term represents an LF function type and returns the
        corresponding argument types.
        """

        (v, a, r) = self.asFunctionType()
        return a

    def getFunctionArity(self):
        """
        Assumes this term represents an LF function type and returns the
        corresponding arity. Equivalent to len(getArgumentTypes()).

        See also: asFunctionType()
        """

        return len(self.getArgumentTypes())

    def getReturnType(self):
        """
        Assumes this term represents an LF function type and returns the
        corresponding return type.

        See also: asFunctionType()
        """
        (v, a, r) = self.asFunctionType()
        return r

    def isBridge():
        """
        Returns True iff this object is a pure Bridge() object.
        """
        return False

    def isTerm():
        """
        Returns True iff this object is a Term() object.
        """
        return True

    def __str__(self):
        return "Term[%r]" % (self.get())
    def __repr__(self):
        return "Term[%r]" % (self.get())
