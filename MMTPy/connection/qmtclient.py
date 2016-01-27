from MMTPy.connection import connection
from MMTPy.query import builder, result
from MMTPy.dependencies import etree

class QMTClient(object):
    """
    Represents a client to the MMT QMT API.
    """

    def __init__(self, url_or_connection):
        """
        Creates a new client to the MMT QMT API
        """

        # Create the connection object
        if isinstance(url_or_connection, connection.Connection):
            self.connection = url_or_connection
        else:
            self.connection = connection.Connection(url_or_connection)
    def queryT(self, url):
        """
        Sends a query to the MMT QMT API and returns html-based text content. 
        """
        (status, txt) = self.connection.getText(url)

        if status == 200:
            return txt
        else:
            return None

    def query(self, query, auto=True):
        """
        Sends a query to the MMT QMT API and returns a (possibly empty) result object
        """

        (status, x) = self.connection.getXML(":query", post_xml=query.toXML())

        if status == 200:
            return result.Result.fromXML(x, auto=auto)
        else:
            return result.Result([], auto=auto)

    def queryOne(self, query, auto=True):
        """
        Sends a query to the MMT QMT API and returns a single result or None
        """

        q = self.query(query, auto=auto)

        if len(q) >= 1:
            return q[0]
        else:
            return None

    def getDeclaration(self, pth):
        """
        Gets the declaration of an object from the MMT API
        """

        return self.queryOne(builder.declaration(pth))

    def getDefinition(self, pth):
        """
        Gets the definition of an object from the MMT API
        """

        decl = self.getDeclaration(pth)

        if decl:
            return decl.df
        else:
            return None
    def getType(self, pth):
        """
        Gets the definitonal type of an object from the MMT API
        """
        decl = self.getDeclaration(pth)

        if decl:
            return decl.tp
        else:
            return None
    def handleLine(self, line):
        """
        Handles a shell command for MMT
        """
        return self.queryT(":action?"+line)
    def present(self, tm, presenter):
        """
        Presents a object (an MMT term) with the specefied presenter
        """
        return self.queryOne(builder.presentation(tm, presenter), auto=False)

    def parse(self, s, thy):
        """
        Parses a string with respect to a certain theory.
        """

        return self.queryOne(builder.parsing(s, thy))

    def infer(self, obj, fnd):
        """
        Infers the type of an object relative to a theory.
        """

        return self.queryOne(builder.infering(obj, fnd))

    def analyze(self, obj, thy):
        """
        Reconstructs the type of an object relative to a theory.
        """

        return self.queryOne(builder.analyzing(obj, thy))

    def simplify(self, obj, thy):
        """
        Simplifies an object with respect to a certain theory.
        """

        return self.queryOne(builder.simplification(obj, thy))
