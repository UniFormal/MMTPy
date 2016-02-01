from MMTPy import xml, metadata

from MMTPy.paths import path
from MMTPy.caseclass import caseclass
from MMTPy.content import vardecl
from MMTPy.content.objects.terms import term

class OML(caseclass.make(vardecl.VarDecl), term.Term):
    """
    An OML wraps a VarDeclaration
    """
    def __init__(self, vd):
        super(OML, self).__init__(vd)
        self.__initmd__()

        self.vd = vd
    def map(self, fn):
        return fn(OML(self.vd.map(fn)))
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

            parsed = OML(vardecl.VarDecl.fromXML(oml))
            parsed.metadata = md

            return parsed
        else:
            raise ValueError("Not a well-formed <OML/>")
