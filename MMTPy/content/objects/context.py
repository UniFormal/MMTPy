from MMTPy import xml, metadata
from MMTPy.caseclass import caseclass

from MMTPy.content.objects import vardecl, obj

class Context(caseclass.make([vardecl.VarDecl]), obj.Obj):
    def __init__(self, variables):
        super(Context, self).__init__(variables)
        self.variables = variables
    def toXML(self):
        return xml.make_element(xml.omt("OMBVAR"), self.toMetaDataXML(), *map(lambda v:v.toXML(), variables))

    @staticmethod
    def fromXML(onode):
        (md, node) = metadata.MetaData.extractMetaDataXML(onode)

        (m, (omv, decls)) = xml.match(node, (xml.omt("OMBVAR"), None))
        if m:
            parsed = Context(list(map(vardecl.VarDecl.fromXML, decls)))
            parsed.metadata = md

            return parsed
        else:
            raise ValueError("Not a well-formed context")
