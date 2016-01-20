from MMTPy import xml, metadata

from MMTPy.objects import path
from MMTPy.objects.terms import term
from MMTPy.caseclass import caseclass

class OMV(caseclass.make(path.LocalName), term.Term):
    def __init__(self, name):
        super(OMV, self).__init__(name)
        self.name = name
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