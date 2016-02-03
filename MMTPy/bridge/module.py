from MMTPy.bridge import bridge
from MMTPy.paths import path
from MMTPy.content.structural.content.modules import module

class Module(bridge.Bridge):
    """
    A Module() object represents a Bridge() that wraps an MMT Module - a theory
    or a view.
    """

    def __init__(self, qclient, mpath, previous = None):
        """
        Creates a new Module() object for MMT. Note that this function should
        never be called manually but always automatically through another
        Bridge() method.

        Arguments:

        qclient
            A QMTClient object representing the connection to MMT.
        mpath
            An MPath to the wrapped module
        previous
            A previous Bridge object (if applicable)
        """

        super(Module, self).__init__(qclient, previous = previous)

        if isinstance(mpath, path.MPath):
            self.__path = mpath
        else:
            raise TypeError("mpath parameter must be an MPath()")

        # retrieve the actual module from MMT
        try:
            o = self.getClient().getDeclaration(self.__path)
        except Exception as e:
            raise ServerSideError(e)

        # raise an Error if this is not a module
        if not isinstance(o, module.Module):
            raise ServerSideError(o)

        self.__module = o

    def __eq__(self, other):
        return isinstance(other, Module) and other.__path == self.__path

    def parent(self):
        """
        Gets the namespace matching to this Module().
        """
        return bridge.Bridge.create(self, self.__path.parent)

    def getModule(self):
        """
        Gets the Module() matching this Module()
        """
        return self

    def getNamespace(self):
        """
        Gets the Namespace() matching this Module()
        """

        return self.parent()

    def get(self):
        """
        Gets the underlying declaration that is wrapped by this Module().
        """

        return self.__module

    def toPath(self):
        """
        Turns this Module() object into a matching Path() object
        """
        return self.__path

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

    def getDeclaration(self, name):
        """
        Gets a declaration of a given item.
        """
        return bridge.Bridge.create(self, self.__path[name])

    def __getitem__(self, name):
        """
        Same as getDeclaration(name)
        """
        return self.getDeclaration(name)

    def __getattr__(self, name):
        """
        Same as getDeclaration(name)
        """
        return self.getDeclaration(name)

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

    def isModule():
        """
        Returns True iff this object is a Module() object.
        """
        return True
