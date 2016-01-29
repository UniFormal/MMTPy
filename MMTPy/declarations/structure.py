from MMTPy import xml, metadata

from MMTPy.paths import path
from MMTPy.caseclass import caseclass
from MMTPy.declarations import declaration

class Structure(caseclass.make(path.MPath), declaration.Declaration):
    def __init__(self, frm):
        super(Structure, self).__init__(frm)
        self.__initmd__()

        self.frm = frm
    def map(self, fn):
        return fn(Structure(self.frm))
    def toXML(self):
        return xml.make_element("import", self.toMetaDataXML(), **{"from": self.frm})

    @staticmethod
    def fromXML(onode):
        (md, node) = metadata.MetaData.extractMetaDataXML(onode)
        if xml.matches(node, "import"):

            parsed = Structure(path.Path.parseM(node.attrib.get("name")))
            parsed.metadata = md

            return parsed
        else:
            raise ValueError("not a well-formed structure (or unsupported import)")
