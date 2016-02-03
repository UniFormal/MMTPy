from MMTPy.bridge import bridge
from MMTPy.paths import path
from MMTPy.content.structural.content.declarations import declaration

class Declaration(bridge.Bridge):
    """
    A Declaration() object represents a Bridge() that wraps an MMT Declaration.
    """

    def __init__(self, bkend, gname, previous = None):
        """
        Creates a new Declaration() object for MMT. Note that this function should
        never be called manually but always automatically through another
        Bridge() method.

        Arguments:

        bkend
            The Backend object used to retrieve objects from MMT.
        gname
            A GlobalName pointing to the declaration.
        previous
            A previous Bridge object (if applicable)
        """

        super(Declaration, self).__init__(bkend, previous = previous)

        if isinstance(gname, path.GlobalName):
            self.__path = gname
        else:
            raise TypeError("gname parameter must be an GlobalName()")

        # TODO: Think about resolving 'aliases' (MMT side)
        # retrieve the actual declaration from MMT
        try:
            o = self.getBackend().getDeclaration(self.__path)
        except Exception as e:
            print(e)
            raise bridge.ServerSideError(e)

        # raise an Error if this is not a module
        if not isinstance(o, declaration.Declaration):
            raise bridge.ServerSideError(o)

        self.__decl = o

    #
    # OWN METHODS
    #

    def getType(self):
        """
        Gets a Term() representing the type of this declaration or None.
        """

        tp_tm = self.get().tp

        if tp_tm == None:
            return None

        return self.set(tp_tm)

    def getDefinition(self):
        """
        Gets a Term() representing the definition of this declaration or None.
        """

        df_tm = self.get().df

        if df_tm == None:
            return None

        return self.set(df_tm)

    #
    # NAVIGATION within the currently wrapped objects
    #

    def parent(self):
        """
        Gets the Module() matching to this Declaration().
        """

        return self.set(self.__path.module)

    def get(self):
        """
        Gets the underlying declaration that is wrapped by this Declaration()
        """

        return self.__decl

    #
    # turn it into path and Term objects
    #

    def toPath(self):
        """
        Turns this Declaration() object into a matching Path() object
        """
        return self.__path

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
    def __eq__(self, other):
        return isinstance(other, Declaration) and other.toPath() == self.toPath()

    #
    # CHECKERS for each type of bridge object
    #

    def isBridge():
        """
        Returns True iff this object is a pure Bridge() object.
        """
        return False

    def isDeclaration():
        """
        Returns True iff this object is a Namespace() object.
        """
        return True

    #
    # GETTERS for each type of bridge object
    #

    def getBridge(self):
        """
        Gets the Bridge() matching this Term()
        """

        return self.parent().parent()

    def getModule(self):
        """
        Gets the Module() matching this Term()
        """
        return self.parent()

    def getDeclaration(self):
        """
        Gets the Declaration() matching this Term()
        """

        return self
