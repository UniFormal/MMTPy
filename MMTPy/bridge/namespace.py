from MMTPy.bridge import bridge
from MMTPy.paths import path

class Namespace(bridge.Bridge):
    """
    A Namespace() object represents a Bridge() that wraps an MMT Namespace
    """

    def __init__(self, qclient, dpath, previous = None):
        """
        Creates a new Namespace() object for MMT. Note that this function should
        never be called manually but always automatically through another
        Bridge() method.

        Arguments:

        qclient
            A QMTClient object representing the connection to MMT.
        dpath
            An DPath to the wrapped module
        previous
            A previous Bridge object (if applicable)
        """

        super(Namespace, self).__init__(qclient, previous = previous)

        if isinstance(dpath, path.DPath):
            self.__path = dpath
        else:
            raise TypeError("dpath parameter must be an DPath()")

    def __eq__(self, other):
        return isinstance(other, Namespace) and other.__path == self.__path

    def getNamespace(self):
        """
        Gets the Namespace() matching this Namespace()
        """

        return self

    def get(self):
        """
        Gets the underlying namespace that is wrapped by this Namespace(). Not
        applicable.
        """

        raise NotImplementedError

    def toPath(self):
        """
        Turns this Namespace() object into a matching Path() object
        """
        raise self.__path

    def navigate(self, pth):
        """
        Navigates this bridge to a given path. Not applicable.
        """

        return bridge.Bridge.create(self, path.Path.parse(str(self.__path) + pth))
    def isBridge():
        """
        Returns True iff this object is a pure Bridge() object.
        """
        return False

    def isNamespace():
        """
        Returns True iff this object is a Namespace() object.
        """
        return True
