from MMTPy import xml, metadata

from MMTPy.objects import context
from MMTPy.caseclass import caseclass
from MMTPy.objects.terms import term

class OMBINDC(caseclass.make(term.Term, context.Context, [term.Term]), term.Term):
    def __init__(self, binder, ctx, scopes):
        super(OMBINDC, self).__init__(binder, scopes)
        self.binder = binder
        self.ctx = ctx
        self.scopes = scopes
    def toXML(self):
        return xml.make_element(xml.omt("OMBINDC"), self.toMetaDataXML(), self.binder.toXML(), self.ctx.toXML(), *map(lambda s:s.toXML(), self.scopes))
    @staticmethod
    def fromXML(onode):
        (md, node) = metadata.MetaData.extractMetaDataXML(onode)

        (m, (ombindc, childs)) = xml.match(node, (xml.omt("OMBINDC"), None))
        if m:
            if len(childs) < 2:
                raise ValueError("Not a well-formed <OMBINDC/>, needed at least 2 children")

            bnd = term.Term.fromXML(childs[0])
            ctx = context.Context.fromXML(childs[1])
            scopes = list(map(term.Term.fromXML, childs[2:]))

            parsed = OMBINDC(bnd, ctx, scopes)
            parsed.metadata = md

            return parsed
        else:
            raise ValueError("Not a well-formed <OMBINDC/>")
