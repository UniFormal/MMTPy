from MMTPy import xml

from MMTPy.paths import uri

from MMTPy.backend import backend
from MMTPy.query import builder, result

import requests
from lxml import etree
from MMTPy.dependencies import etree_type

class QMTBackend(backend.Backend):
    """
    Represents an Abstract Backend to MMT.
    """
    def __init__(self, url):
        """
        Creates a new client to the MMT QMT API
        """

        super(QMTBackend, self).__init__()

        # parse the baseURI
        uriobj = uri.URI.parse(url)

        # and extract only the parts we want
        self.__base = uriobj.scheme + "://" + uriobj.authority + "/"

    #
    # HTTP connection methods
    #
    def get(self, pth, post_xml=None):
        """
        Makes a GET or POST request to the given pth
        """

        fullpth = self.__base + pth

        if post_xml == None:
            res = requests.get(fullpth)
        else:
            # turn the xml we want to send into a string
            pxml = etree.tostring(post_xml) if isinstance(post_xml, etree_type) else post_xml

            # then make the request
            res = requests.post(fullpth, headers={'Content-Type': 'application/xml'}, data=pxml)
        return (res.status_code, res.text)

    def getXML(self, pth, post_xml=None):
        """
        Makes a GET request to MMT, parses XML and return (statusCode, xml)
        """

        (code, txt) = self.get(pth, post_xml=post_xml)
        return (code, etree.fromstring(txt))

    def getText(self, pth, post_xml=None):
        """
        Makes GET request to MMT, parses it as HTML and returns (statusCode, text)
        """
        (code, x) = self.getXML(pth, post_xml=post_xml)
        return (code, xml.textcontent(x))

    #
    # QMT query methods
    #
    def query(self, query, auto=True):
        """
        Sends a query to the MMT QMT API and returns a (possibly empty) result object
        """

        (status, x) = self.getXML(":query", post_xml=query.toXML())

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

    def queryT(self, url):
        """
        Sends a query to the MMT QMT API and returns html-based text content.
        """
        (status, txt) = self.connection.getText(url)

        if status == 200:
            return txt
        else:
            return None



    #
    # DECLARATION
    #
    def getDeclaration(self, pth):
        """
        Gets the declaration of the ContentElement pointed to by pth.
        """

        return self.queryOne(builder.presentationDecl(pth, "xml"))

    #
    # PRESENTATION
    #
    def present(self, tm, presenter="xml"):
        """
        Presents a object (an MMT term) with the specefied presenter.
        """
        return self.queryOne(builder.presentation(tm, presenter), auto=False)

    def presentDeclaration(self, pth, presenter="xml"):
        """
        Presents the declaration of an object with the specefied presenter.
        """
        return self.queryOne(builder.presentationDecl(tm, presenter), auto=False)

    #
    # PARSING
    #

    def parse(self, s, thy):
        """
        Parses a string with respect to a certain theory.
        """

        return self.queryOne(builder.parsing(s, thy))

    #
    # SIMPLIFICATION
    #
    def simplify(self, obj, thy):
        """
        Simplifies an object with respect to a certain theory.
        """

        return self.queryOne(builder.simplification(obj, thy))

    #
    # TYPE INFERENCE
    #

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

    #
    # MISC
    #
    def handleLine(self, line):
        """
        Handles a shell command for MMT
        """
        return self.queryT(":action?"+line)
