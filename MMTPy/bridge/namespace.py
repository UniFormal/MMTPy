from MMTPy.bridge import bridge
from MMTPy.paths import path

class Namespace(bridge.Bridge):
    """
    A Namespace() object represents a Bridge() that wraps an MMT Namespace
    """

    def __init__(self, bkend, dpath, previous = None):
        """
        Creates a new Namespace() object for MMT. Note that this function should
        never be called manually but always automatically through another
        Bridge() method.

        Arguments:

        bkend
            The Backend object used to retrieve objects from MMT.
        dpath
            An DPath to the wrapped module
        previous
            A previous Bridge object (if applicable)
        """

        super(Namespace, self).__init__(bkend, previous = previous)

        if isinstance(dpath, path.DPath):
            self.__path = dpath
        else:
            raise TypeError("dpath parameter must be an DPath()")

    #
    # OWN METHODS
    #

    #
    # NAVIGATION within the currently wrapped objects
    #

    def parent(self):
        """
        Gets the Bridge() matching to this Namespace().
        """
        return self.set(None)

    def get(self):
        """
        Gets the underlying namespace that is wrapped by this Namespace(). Not
        applicable.
        """

        raise NotImplementedError

    #
    # turn it into path and Term objects
    #

    def toPath(self):
        """
        Turns this bridge object into a matching Path() object
        """
        return self.__path

    #
    # NAVIGATION + aliases
    #

    def navigate(self, pth):
        """
        Navigates this bridge to a given path. Not applicable.
        """
        pstring = path.Path.parse(str(self.__path) + "?" + pth)
        try:
            return self.set(pstring)
        except Exception as e:
            print(pstring)
            raise


    def getTheory(self, pth):
        """
        Navigates this bridge to a given path and ensures that the returned
        Module() object is a theory.
        """

        pt = self.navigate(pth)

##        if not pt.isTheory():
#            print(pt)
#            print(pt.get())
#            raise ValueError("Given path does not point to a Theory")
        return pt

    def getView(self, pth):
        """
        Navigates this bridge to a given path and ensures that the returned
        Module() object is a view.
        """

        pt = self.navigate(pth)

        if not pt.isView():
            raise ValueError("Given path does not point to a View")

        return pt

    #
    # STRINGs + EQUALITY
    #
    def __eq__(self, other):
        return isinstance(other, Namespace) and other.toPath() == self.toPath()

    #
    # CHECKERS for each type of bridge object
    #
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

    #
    # GETTERS for each type of bridge object
    #
    def getBridge(self):
        """
        Gets the Bridge() matching this Namespace()
        """

        return self.parent()

    def getNamespace(self):
        """
        Gets the Namespace() matching this Namespace()
        """

        return self
