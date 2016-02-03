from MMTPy.caseclass import types
from MMTPy.connection import qmtclient
from MMTPy.paths import path
from MMTPy.content.objects.terms import term
from MMTPy.utils import ustr

class Bridge(object):
    """
    A Bridge() represents a human friendly connetion interface to MMT.
    It must be one of the following 5 types:

    1. A Bridge() object (nothing)
    2. A Namespace() object (path in which theories + modules live)
    3. A Module() object (theories + views)
    4. A Declaration() object (constant declarations + imports )
    5. A Term() object (objects within MMT)
    """

    def __init__(self, qclient, previous = None):
        """
        Creates a new Bridge() object for MMT. Note that this function should
        never be called manually but always automatically through the Bridge.create()
        method.

        Arguments:

        qclient
            A QMTClient object representing the connection to MMT.
        previous
            A previous Bridge object (if applicable)
        """

        if isinstance(qclient, qmtclient.QMTClient):
            self.__qclient = qclient
        else:
            raise TypeError("qclient parameter must be a QMTClient. ")

        if previous != None:
            if isinstance(previous, Bridge):
                self.__previous = previous
            else:
                TypeError("previous parameter must be a Bridge() or None. ")
    def getClient(self):
        """
        Returns the QClient associated to this Bridge() instance.
        """
        return self.__qclient

    def previous(self):
        """
        Retrieves the previous Bridge() object that was used to create this
        one or raises a NoPreviousException()
        """

        if self.__previous != None:
            return self.__previous

        raise NoPreviousException()

    def parent(self):
        """
        Retrieves a parent Bridge object representing one semantic level
        above the current one or raises a NoParentException()
        """

        raise NoParentException()

    def getDeclaration(self):
        """
        Gets the Declaration() matching this Bridge().
        """

        raise NotImplementedError

    def getModule(self):
        """
        Gets the Module() matching this Bridge().
        """

        raise NotImplementedError

    def getNamespace(self):
        """
        Gets the Namespace() matching this Bridge().
        """

        raise NotImplementedError


    def get(self):
        """
        Gets the underlying object that is wrapped by this Bridge()
        """

        raise NoWrappedException()

    def toPath(self):
        """
        Turns this bridge object into a matching Path() object
        """
        return path.Path.parse("")

    def toTerm(self):
        """
        Turns this Bridge() object into a corresponding Term() object, namely
        as OMID(self.toPath())
        """
        
        return Bridge.create(self, self.toPath().toTerm())

    def navigate(self, pth):
        """
        Navigates this client to a given path.
        """

        return Bridge.create(self, path.Path.parse(pth))

    def __call__(self, other):
        """
        Same as navigate()
        """
        return self.navigate(other)

    def __str__(self):
        return "%s[%r]" % (self.__class__.__name__, str(self.toPath()))
    def __repr__(self):
        return "%s[%r]" % (self.__class__.__name__, str(self.toPath()))

    def isBridge():
        """
        Returns True iff this object is a pure Bridge() object.
        """
        return True

    def isNamespace():
        """
        Returns True iff this object is a Namespace() object.
        """
        return False
    def isModule():
        """
        Returns True iff this object is a Module() object.
        """
        return False
    def isDeclaration():
        """
        Returns True iff this object is a Declaration() object.
        """
        return False
    def isTerm():
        """
        Returns True iff this object is a Term() object.
        """
        return False

         Bridge() object (nothing)
        2. A Namespace() object (path in which theories + modules live)
        3. A Module() object (theories + views)
        4. A Declaration() object (constant declarations + imports )
        5. A Term() object (objects within MMT)

    @staticmethod
    def create(connection_or_bridge, path_or_term = None):
        """
        Creates a new instance of the Bridge() class (or the appropriate
        subclass). This is done by requesting the appropriate definition
        from MMT and instantiating the right subclass.

        Arguments:

        connection_or_bridge
            Connection or Bridge() object that represents the connection to
            MMT.

        path_or_term
            Optional. Either a path to the object to wrap or a path to the

        """

        # first we need to parse the connection object and set a previous object
        # we support either a previous Bridge(), a QMTClient() or anything that
        # the QMTClient() constructor takes
        if isinstance(connection_or_bridge, Bridge):
            qclient = connection_or_bridge.getClient()
            previous = connection_or_bridge
        elif isinstance(connection_or_bridge, qmtclient.QMTClient):
            qclient = connection_or_bridge
            previous = None
        else:
            qclient = qmtclient.QMTClient(connection_or_bridge)
            previous = None

        # next we need to parse the object we are wrapping
        # if this is empty, we can return immmediatly with either an empty MMT
        # object or a term.
        if path_or_term == None or ustr(path_or_term) == "":
            if previous != None:
                return previous
            else:
                return Bridge(qclient)

        # if we have a path instance, we need to figure out what type it is and
        # wrap it in the matching object
        if isinstance(path_or_term, path.Path):
            if isinstance(path_or_term, path.MPath):
                from MMTPy.bridge import module
                return module.Module(qclient, path_or_term, previous = previous)
            elif isinstance(path_or_term, path.GlobalName):
                from MMTPy.bridge import declaration
                return declaration.Declaration(qclient, path_or_term, previous = previous)
            elif isinstance(path_or_term, path.DPath):
                from MMTPy.bridge import namespace
                return namespace.Namespace(qclient, path_or_term, previous = previous)

            raise ValueError("Bridge() can not wrap unknown Path() object %r" % path_or_term)

        # if it is a term we can wrap it in an objects object
        if isinstance(path_or_term, term.Term):
            from MMTPy.bridge import term as bterm
            return bterm.Term(qclient, path_or_term, previous = previous)

        # If it is neither one of the above we want to parse the path as a
        # string and then try again.
        return Bridge(connection_or_bridge, path.Path.parse(path_or_term))


class NoParentException(Exception):
    """
    Exception that is thrown when a user tries to call parent() on a parent-less
    Bridge().
    """
    def __init__(self):
        super(NoParentException, self).__init__("Can not call parent() on a parent-less Bridge() object. ")

class NoPreviousException(Exception):
    """
    Exception that is thrown when a user tries to call previous() on a
    previous-less Bridge().
    """
    def __init__(self):
        super(NoParentException, self).__init__("Can not call previous() on a previous-less Bridge() object. ")

class NoWrappedException(Exception):
    """
    Exception that is thrown when a user tries to call get() on a pure bridge object.
    """
    def __init__(self):
        super(NoParentException, self).__init__("Can not call get() on a non-wrapping Bridge() object. ")
class ServerSideError(Exception):
    def __init__(self, err):
        self.error = err
        super(NoParentException, self).__init__("Error retrieving selected object from server: %s" % self.error)
