from MMTPy import xml

from MMTPy.objects.URI import URI
from MMTPy.dependencies import requests, etree

from MMTPy.query import builder, result

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

    def getXML(self, pth, post_xml=None):
        """
        Makes a GET request to MMT, parses XML and return (statusCode, xml)
        """
        (code, txt) = self.get(pth, post_xml=post_xml)
        return (code, etree.fromstring(txt))
    
    def query(self, query):
        """
        Sends a query to the MMT API and parses the response. 
        """
        
        (status, x) = self.getXML(":query", post_xml=etree.tostring(query.toXML()))
        
        if status == 200:
            return result.Result.fromXML(x)
        else:
            return result.Result([])

    def getDeclaration(self, pth):
        """
        Gets a declaration of an object the MMT API.
        """
        return self.query(builder.declaration(pth))
