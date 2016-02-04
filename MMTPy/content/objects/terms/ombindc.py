from MMTPy import xml, metadata

from MMTPy.content.objects import context
from MMTPy.clsutils import caseclass, types
from MMTPy.content.objects.terms import term

@caseclass.caseclass
@types.argtypes(term.Term, context.Context, [term.Term])
class OMBINDC(term.Term):
    def __init__(self, binder, ctx, scopes):
        term.Term.__init__(self)

        self.binder = binder
        self.ctx = ctx
        self.scopes = scopes
    def toXML(self):
        return xml.make_element(xml.omt("OMBIND"), self.toMetaDataXML(), self.binder.toXML(), self.ctx.toXML(), *map(lambda s:s.toXML(), self.scopes))
    def map(self, fn):
        ab = self.binder.map(fn)
        sc = self.ctx.map(fn)
        ss = self.scopes.map(fn)

        return fn(OMBINDC(ab, sc, ss))
    @staticmethod
    def fromXML(onode):
        (md, node) = metadata.MetaData.extractMetaDataXML(onode)

        (m, (ombindc, childs)) = xml.match(node, (xml.omt("OMBIND"), None))
        if m:
            if len(childs) < 2:
                raise ValueError("Not a well-formed <OMBIND/>, needed at least 2 children")

            bnd = term.Term.fromXML(childs[0])
            ctx = context.Context.fromXML(childs[1])
            scopes = list(map(term.Term.fromXML, childs[2:]))

            parsed = OMBINDC(bnd, ctx, scopes)
            parsed.metadata = md

            return parsed
        else:
            raise ValueError("Not a well-formed <OMBIND/>")
