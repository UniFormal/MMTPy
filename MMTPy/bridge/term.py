from MMTPy.bridge import bridge
from MMTPy.content.objects.terms import term
from MMTPy.library.lf import wrappers

class Term(bridge.Bridge):
    """
    An Term() object represents a Bridge() that wraps an MMT Object.
    """

    def __init__(self, bkend, tm, previous = None):
        """
        Creates a new Term() object for MMT. Note that this function should
        never be called manually but always automatically through another
        Bridge() method.

        Arguments:

        bkend
            The Backend object used to retrieve objects from MMT.
        tm
            A Term containing the actual declaration
        previous
            A previous Bridge object (if applicable)
        """

        super(Term, self).__init__(bkend, previous = previous)

        if isinstance(tm, term.Term):
            self.__tm = tm
        else:
            raise TypeError("tm parameter must be an Term()")

        from MMTPy.bridge import declaration
        if isinstance(previous, declaration.Declaration):
            self.__gn = previous.toPath()
        else:
            self.__gn = None

    #
    # OWN METHODS
    #

    def asFunctionType(self):
        """
        Assumes this term represents an LF function type and returns a triple
        (variables, argument_types, return_type)
        """

        (v, a, r) = wrappers.lf_unpack_function_types(self.get())

        return (v, [self.set(aa) for aa in a], self.set(r))


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

    #
    # NAVIGATION within the currently wrapped objects
    #

    def parent(self):
        """
        Gets the Declaration() matching this Term().
        """

        if self.__gn == None:
            raise bridge.NoParentException()

        return self.set(self.__gn)

    def get(self):
        """
        Gets the underlying term that is wrapped by this Term().
        """

        return self.__tm

    #
    # turn it into path and Term objects
    #

    def toPath(self):
        """
        Turns this Term() object into a matching Path() object
        """
        return self.__gn

    #
    # NAVIGATION + aliases
    #

    def navigate(self, pth):
        """
        Navigates this bridge to a given path. Not applicable.
        """

        raise NotImplementedError

    #
    # STRINGs + EQUALITY
    #
    def __str__(self):
        return "Term[%r]" % (self.get())
    def __repr__(self):
        return "Term[%r]" % (self.get())
    def __eq__(self, other):
        return isinstance(other, Term) and other.get() == self.get()

    #
    # CHECKERS for each type of bridge object
    #

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

    #
    # GETTERS for each type of bridge object
    #
    def getBridge(self):
        """
        Gets the Namespace() matching this Term()
        """

        return self.parent().parent().parent().parent()
    def getNamespace(self):
        """
        Gets the Namespace() matching this Term()
        """

        return self.parent().parent().parent()
    def getModule(self):
        """
        Gets the Module() matching this Term()
        """
        return self.parent().parent()

    def getDeclaration(self):
        """
        Gets the Declaration() matching this Term()
        """

        return self.parent()
