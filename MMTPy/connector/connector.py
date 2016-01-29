from MMTPy.caseclass import types
from MMTPy.connection import qmtclient
from MMTPy.paths import path
from MMTPy.content.objects.terms import term
from MMTPy.utils import ustr

class Connector(object):
    """
    A Connector() represents a human friendly connetion interface to MMT.
    It must be one of the following 4 types:

    1. A Connector() object (representing a connection to MMT without any
       set parent path)
    2. A Module() object (representing a module in MMT that can contain several
       theories in MMT)
    3. A Declaration() object (representing any declaration with any MMT module or
       or nested with another declaration)
    4. A Term() object (representing any term in MMT)
    """

    def __init__(self, qclient, previous = None):
        """
        Creates a new Connector() object for MMT. Note that this function should
        never be called manually but always automatically through the __new__()
        method.

        Arguments:

        qclient
            A QMTClient object representing the connection to MMT.
        previous
            A previous Connector object (if applicable)
        """

        if isinstance(qclient, qmtclient.QMTClient):
            self.__qclient = qclient
        else:
            raise TypeError("qclient parameter must be a QMTClient. ")

        if previous != None:
            if isinstance(previous, Connector):
                self.__previous == previous
            else:
                TypeError("previous parameter must be a Connector() or None. ")

    def previous(self):
        """
        Retrieves the previous Connector() object that was used to create this
        one or raises a NoPreviousException()
        """

        if self.__previous != None:
            return self.__previous

        raise NoPreviousException()

    def parent(self):
        """
        Retrieves a parent Connector object representing one semantic level
        above the current one or raises a NoParentException()
        """

        raise NoParentException()

    def __new__(cls, connection_or_connector, path_or_term = None):
        """
        Creates a new instance of the Connector() class (or the appropriate
        subclass). This is done by requesting the appropriate definition
        from MMT and instantiating the right subclass.

        Arguments:

        connection_or_connector
            Connection or Connector() object that represents the connection to
            MMT.

        path_or_term
            Optional. Either a path to the object to wrap or a path to the

        """

        # first we need to parse the connection object and set a previous object
        # we support either a previous Connector(), a QMTClient() or anything that
        # the QMTClient() constructor takes
        if isinstance(connection_or_connector, Connector):
            qclient = connection_or_connector.qclient
            previous = connection_or_connector
        elif isinstance(connection_or_connector, qmtclient.QMTClient):
            qclient = connection_or_connector
            previous = None
        else:
            qclient = qmtclient.QMTClient(connection_or_connector)
            previous = None

        # next we need to parse the object we are wrapping
        # if this is empty, we can return immmediatly with either an empty MMT
        # object or a term.
        if path_or_term == None or ustr(path_or_term) == "":
            if previous != None:
                return previous
            else:
                return super(Connector,self).__new__(self, qclient)

        # if we have a path instance, we need to figure out what type it is and
        # wrap it in the matching object
        if isinstance(path_or_term, path.Path):
            if isinstance(path_or_term, path.DPath):
                pass # TODO: Make a module
            elif isinstance(path_or_term, path.ContentPath):
                pass # TODO: Make a declaration

            raise ValueError("Connector() can not wrap unknown Path() object %r" % path_or_term)

        # if it is a term we can wrap it in an objects object
        if isinstance(path_or_term, term.Term):
            pass # TODO: Make an object

        # If it is neither one of the above we want to parse the path as a
        # string and then try again.
        return Connector(connection_or_connector, path.Path.parse(path_or_term))


class NoParentException(Exception):
    """
    Exception that is thrown when a user tries to call parent() on a parent-less
    object.
    """
    def __init__(self):
        super(NoParentException, self).__init__("Can not call parent() on a parent-less Connector() object. ")

class NoPreviousException(Exception):
    """
    Exception that is thrown when a user tries to call previous() on a
    previous-less object.
    """
    def __init__(self):
        super(NoParentException, self).__init__("Can not call previous() on a previous-less Connector() object. ")
