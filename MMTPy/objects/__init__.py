from MMTPy import xml

class Object(object):
    def __init__(self):
        self.metadata = None
    def toMetaDataXML(self):
        return xml.make_element("metadata")
    @staticmethod
    def parseMetaDataXML(node):
        for c in node:
            (m, md) = xml.match(node, "metadata")
            if m:
                node.remove()
        # TODO: Actually parse the meta-data
        # but lets leave that for now
        return None
