from MMTPy import xml

from MMTPy.objects.URI import URI
from MMTPy.declarations import declaration
from MMTPy.dependencies import requests, etree

from MMTPy.query import builder 

class Connection():
    """
    Represents a connection to MMT
    """
    def __init__(self, baseURI):

        # parse the baseURI
        uriobj = URI.parse(baseURI)

        # and extract only the parts we want
        self.base = uriobj.scheme + "://" + uriobj.authority + "/"

    def get(self, pth, post_xml=None):
        """
        Makes a GET or POST request to the given pth
        """
        
        fullpth = self.base + pth
        
        if post_xml == None:
            res = requests.get(fullpth)
        else:
            res = requests.post(fullpth, headers={'Content-Type': 'application/xml'}, data=post_xml)
        return (res.status_code, res.text)

    def getXML(self, pth):
        """
        Makes a GET request to MMT, parses XML and return (statusCode, xml)
        """
        (code, txt) = self.get(pth)
        return (code, etree.fromstring(txt))
    def getDeclarationXML(self, pth):
        """
        Gets the XML of a declaration from the MMT HTTP API
        """
        # build the path to request from MMT
        s_path = ":mmt?get "+str(pth)+" present xml respond"

        # make the request and return it
        return self.getXML(s_path)
    
    def query(self, query):
        """
        Sends a query object to the MMT API and returns a string representing the response. 
        """
        
        return self.get(":query", post_xml=etree.tostring(query.toXML()))

    def getDeclaration(self, pth):
        """
        Gets a declaration of an object the MMT API.
        """
        return self.query(builder.declaration(pth))
