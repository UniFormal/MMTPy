from MMTPy import metadata
from MMTPy import xml

class Obj(metadata.MetaData):
    def __init__(self):
        super(Obj, self).__init__()
    def toOBJXML(self):
        nowrapnode = self.toXML()
        return xml.make_element(xml.omt("OMOBJ"), nowrapnode)