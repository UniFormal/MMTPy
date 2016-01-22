from MMTPy import xml

from MMTPy.objects.URI import URI
from MMTPy.dependencies import requests, etree, etree_type

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
