from MMTPy import xml, metadata

from MMTPy.paths import path
from MMTPy.content.objects.terms import term
from MMTPy.clsutils import caseclass, types

@caseclass.caseclass
@types.argtypes(path.LocalName)
class OMV(term.Term):
    def __init__(self, name):
        super(OMV, self).__init__()

        self.name = name
    def map(self, fn):
        return fn(OMV(self.name))
    def toXML(self):
        return xml.make_element(xml.omt("OMV"), self.toMetaDataXML(), name=self.name)
    @staticmethod
    def fromXML(onode):
        (md, node) = metadata.MetaData.extractMetaDataXML(onode)
        (m, omv) = xml.match(node, xml.omt("OMV"))
        if m:
            pth = path.LocalName.parse(node.attrib.get("name"))

            parsed = OMV(pth)
            parsed.metadata = md

            return parsed
        else:
            raise ValueError("Not a well-formed <OMV/>")
