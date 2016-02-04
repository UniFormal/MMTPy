from MMTPy import xml, metadata
from MMTPy.clsutils import caseclass, types

from MMTPy.content.objects import vardecl, obj

@caseclass.caseclass
@types.argtypes([vardecl.VarDecl])
class Context(obj.Obj):
    def __init__(self, variables):
        obj.Obj.__init__(self)
        
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
