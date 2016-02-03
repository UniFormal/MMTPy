from MMTPy.bridge import bridge
from MMTPy.paths import path
from MMTPy.content.structural.content.modules import module

class Module(bridge.Bridge):
    """
    A Module() object represents a Bridge() that wraps an MMT Module - a theory
    or a view.
    """

    def __init__(self, bkend, mpath, previous = None):
        """
        Creates a new Module() object for MMT. Note that this function should
        never be called manually but always automatically through another
        Bridge() method.

        Arguments:

        bkend
            The Backend object used to retrieve objects from MMT.
        mpath
            An MPath to the wrapped module
        previous
            A previous Bridge object (if applicable)
        """

        super(Module, self).__init__(bkend, previous = previous)

        if isinstance(mpath, path.MPath):
            self.__path = mpath
        else:
            raise TypeError("mpath parameter must be an MPath()")

        # retrieve the actual module from MMT
        try:
            o = self.getBackend().getDeclaration(self.__path)
        except Exception as e:
            raise ServerSideError(e)

        # raise an Error if this is not a module
        if not isinstance(o, module.Module):
            raise ServerSideError(o)

        self.__module = o

    #
    # OWN METHODS
    #


    def isTheory(self):
        """
        Checks if this Module() represents a theory.
        """

        from MMTPy.content.structural.content.modules import theory
        return isinstance(self.get(), theory.Theory)

    def isView(self):
        """
        Checks if this Module() represents a view.
        """

        from MMTPy.content.structural.content.modules import view
        return isinstance(self.get(), view.View)

    #
    # DELEGATED METHODS
    #

    def asFunctionType(self):
        """
        Assumes the type of this declaration represents an LF function type and returns a triple
        (variables, argument_types, return_type)
        """

        return self.getType().asFunctionType()


    def getArgumentTypes(self):
        """
        Assumes the type of this declaration represents an LF function type and returns the
        corresponding argument types.
        """

        return self.getType().getArgumentTypes()

    def getFunctionArity(self):
        """
        Assumes the type of this declaration represents an LF function type and returns the
        corresponding arity. Equivalent to len(getArgumentTypes()).

        See also: asFunctionType()
        """

        return self.getType().getFunctionArity()

    def getReturnType(self):
        """
        Assumes the type of this declaration represents an LF function type and returns the
        corresponding return type.

        See also: asFunctionType()
        """

        return self.getType().getReturnType()

    #
    # NAVIGATION within the currently wrapped objects
    #

    def parent(self):
        """
        Gets the Namespace() matching to this Module().
        """
        return self.set(self.__path.parent)

    def get(self):
        """
        Gets the underlying declaration that is wrapped by this Module().
        """

        return self.__module

    #
    # turn it into path and Term objects
    #

    def toPath(self):
        """
        Turns this Module() object into a matching Path() object
        """
        return self.__path

    #
    # NAVIGATION + aliases
    #

    def navigate(self, name):
        """
        Same as self.getDeclaration
        """
        return self.getDeclaration(name)

    def getDeclaration(self, name):
        """
        Gets a declaration of a given item.
        """

        return self.set(self.__path[name])

    #
    # STRINGs + equality
    #
    def __eq__(self, other):
        return isinstance(other, Module) and other.toPath() == self.toPath()

    #
    # CHECKERS for each type of bridge object
    #
    def isBridge():
        """
        Returns True iff this object is a pure Bridge() object.
        """
        return False

    def isModule():
        """
        Returns True iff this object is a Module() object.
        """
        return True

    #
    # GETTERS for each type of bridge object
    #

    def getBridge(self):
        """
        Gets the Bridge() matching to this Module()
        """

        return self.parent().parent()

    def getNamespace(self):
        """
        Gets the Namespace() matching this Module()
        """

        return self.parent()

    def getModule(self):
        """
        Gets the Module() matching this Module()
        """
        return self
