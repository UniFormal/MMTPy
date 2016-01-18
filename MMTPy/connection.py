from MMTPy.objects.URI import URI
from MMTPy.declarations import declaration

from MMTPy.dependencies import requests, etree
from MMTPy import xml

class Connection():
    """
    Represents a connection to MMT
    """
    def __init__(self, baseURI):

        # parse the baseURI
        uriobj = URI.parse(baseURI)

        # and extract only the parts we want
        self.base = uriobj.scheme + "://" + uriobj.authority + "/"

    def get(self, pth):
        """
        Makes a GET request to MMT and returns (statusCode, text).
        """
        fullpth = self.base + pth
        res = requests.get(fullpth)
        return (res.status_code, res.text)

    def getXML(self, pth):
        """
        Makes a GET request to MMT, parses XML and return (statusCode, xml)
        """
        (code, txt) = self.get(pth)
        return (code, etree.fromstring(txt))
    def getDeclaration(self, pth):
        """
        Gets a declaration of an object the MMT API.
        """

        # build the path to request from MMT
        s_path = ":mmt?get "+str(pth)+" present xml respond"

        # make the request
        (code, pxml) = self.getXML(s_path)

        # if we were not ok, return NOthing
        if code != 200:
            return None

        # else return the theory
        return declaration.Declaration.fromXML(pxml)
