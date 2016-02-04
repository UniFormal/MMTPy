from MMTPy import xml, metadata

from MMTPy.paths import path
from MMTPy.clsutils import caseclass, types
from MMTPy.content.objects.terms import term

from MMTPy.utils import ustr

@caseclass.caseclass
@types.argtypes(path.ContentPath)
class OMID(term.Term):
    """
    An OMID is a case class that references MMT Content by a ContentPath.
    """
    
    def __init__(self, path):
        term.Term.__init__(self)

        self.path = path
    def toXML(self):
        return xml.make_element(xml.omt("OMS"), self.toMetaDataXML(), base=self.path.module.parent, module=self.path.module.name, name=self.path.name)
    def map(self, fn):
        return fn(OMID(self.path))
    def __repr__(self):
        return "OMID[%r]" % (ustr(self.path))
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
