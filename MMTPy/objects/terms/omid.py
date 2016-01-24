from MMTPy import xml, metadata

from MMTPy.objects import path
from MMTPy.caseclass import caseclass
from MMTPy.objects.terms import term

class OMID(caseclass.make(path.ContentPath), term.Term):
    def __init__(self, path):
        super(OMID, self).__init__(path)
        self.__initmd__()

        self.path = path
    def toXML(self):
        return xml.make_element(xml.omt("OMS"), self.toMetaDataXML(), base=self.path.module.parent, module=self.path.module.name, name=self.path.name)
    def map(self, fn):
        return fn(OMID(self.path))
    @staticmethod
    def fromXML(onode):
        (md, node) = metadata.MetaData.extractMetaDataXML(onode)
        (m, oms) = xml.match(node, xml.omt("OMS"))
        if m:
            pth = path.Path.parse((node.attrib.get("base"), node.attrib.get("module"), node.attrib.get("name"), ""), isSplit=True)

            parsed = OMID(pth)
            parsed.metadata = md

            return parsed
        else:
            raise ValueError("Not a well-formed <OMS/>")
