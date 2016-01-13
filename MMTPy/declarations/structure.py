from MMTPy.declarations import declaration
from MMTPy.objects import path

from MMTPy import metadata
from MMTPy import xml
from MMTPy import utils

class Structure(utils.caseClass("Structure", path.MPath), declaration.Declaration):
    def __init__(self, frm):
        super(Structure, self).__init__(frm)
        self.__initmd__()

        self.frm = frm

    def toXML(self):
        return xml.make_element("import", self.toMetaDataXML(), **{"from": self.frm})

    @staticmethod
    def fromXML(onode):
        (md, node) = metadata.MetaData.parseMetaDataXML(onode)
        if xml.matches(node, "import"):

            parsed = Structure(path.Path.parseM(node.attrib.get("name")))
            parsed.metadata = md

            return parsed
        else:
            raise ValueError("not a well-formed structure (or unsupported import)")
