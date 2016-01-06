from MMTPy.objects.URI import URI

from MMTPy.dependencies import requests
from MMTPy import xml

class Connection():
    """
        Represents a connection to MMT
    """
    def __init__(self, baseURI):
        
        # parse the baseURI
        uriobj = URI.fromstring(baseURI)
        
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
        return (code, ET.fromstring(txt))