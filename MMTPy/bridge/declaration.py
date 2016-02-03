from MMTPy.bridge import bridge
from MMTPy.paths import path
from MMTPy.content.structural.content.declarations import declaration

class Declaration(bridge.Bridge):
    """
    A Declaration() object represents a Bridge() that wraps an MMT Declaration.
    """

    def __init__(self, qclient, gname, previous = None):
        """
        Creates a new Declaration() object for MMT. Note that this function should
        never be called manually but always automatically through another
        Bridge() method.

        Arguments:

        qclient
            A QMTClient object representing the connection to MMT.
        gname
            A GlobalName pointing to the declaration.
        previous
            A previous Bridge object (if applicable)
        """

        super(Declaration, self).__init__(qclient, previous = previous)

        if isinstance(gname, path.GlobalName):
            self.__path = gname
        else:
            raise TypeError("gname parameter must be an GlobalName()")
        
        # TODO: Think about resolving 'aliases' (MMT side)
        # retrieve the actual declaration from MMT
        try:
            o = self.getClient().getDeclaration(self.__path)
        except Exception as e:
            raise ServerSideError(e)

        # raise an Error if this is not a module
        if not isinstance(o, declaration.Declaration):
            raise ServerSideError(o)

        self.__decl = o

    def __eq__(self, other):
        return isinstance(other, Declaration) and other.__path == self.__path

    def parent(self):
        """
        Gets the namespace matching to this Module().
        """
        return bridge.Bridge.create(self, self.__path.module)

    def getDeclaration(self):
        """
        Gets the Declaration() matching this Term()
        """

        return self

    def getModule(self):
        """
        Gets the Module() matching this Term()
        """
        return self.parent()

    def get(self):
        """
        Gets the underlying declaration that is wrapped by this Declaration()
        """

        return self.__decl

    def toPath(self):
        """
        Turns this Declaration() object into a matching Path() object
        """
        return self.__path

    def getType(self):
        """
        Gets a Term() representing the type of this declaration or None.
        """

        tp_tm = self.get().tp

        if tp_tm == None:
            return None

        return bridge.Bridge.create(self, tp_tm)

    def getDefinition(self):
        """
        Gets a Term() representing the definition of this declaration or None.
        """

        df_tm = self.get().df

        if df_tm == None:
            return None

        return bridge.Bridge.create(self, df_tm)

    def navigate(self, pth):
        """
        Navigates this bridge to a given path. Not applicable.
        """

        raise NotImplementedError

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
