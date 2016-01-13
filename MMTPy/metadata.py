from MMTPy import xml

class MetaData(object):
    def __init__(self):
        self.__initmd__()
    def __initmd__(self):
        self.metadata = None
    def toMetaDataXML(self):
        return xml.make_element("metadata")
    @staticmethod
    def parseMetaDataXML(onode):

        node = xml.copy(onode)

        for c in node:
            (m, md) = xml.match(c, "metadata")
            if m:
                node.remove(c)

        return (None, node)
