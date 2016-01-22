from MMTPy import xml, metadata

from MMTPy.objects import path
from MMTPy.caseclass import caseclass
from MMTPy.objects import context
from MMTPy.objects.terms import term

class OML(caseclass.make(context.VarDecl), term.Term):
    def __init__(self, vd):
        super(OML, self).__init__(vd)
        self.vd = vd
    def toXML(self):
        vdx = self.vd.toXML()
        vdx.tag = xml.omt("OML")
        return vdx

    @staticmethod
    def fromXML(onode):
        (md, node) = metadata.MetaData.extractMetaDataXML(onode)
        (m, oml) = xml.match(node, xml.omt("OML"))
        if m:
            oml.tag = xml.omt("OMV")
            
            parsed = OML(context.VarDecl.fromXML(oml))
            parsed.metadata = md

            return parsed
        else:
            raise ValueError("Not a well-formed <OML/>")
