from MMTPy import xml, metadata

from MMTPy.objects import path
from MMTPy.caseclass import caseclass
from MMTPy.objects.terms import term

class OMA(caseclass.make(term.Term, [term.Term]), term.Term):
    def __init__(self, fun, args):
        super(OMA, self).__init__(fun, args)
        self.fun = fun
        self.args = args
    def toXML(self):
        return xml.make_element(xml.omt("OMA"), self.toMetaDataXML(), self.fun.toXML(), *map(lambda a:a.toXML(), self.args))

    @staticmethod
    def fromXML(onode):
        (md, node) = metadata.MetaData.extractMetaDataXML(onode)
        (m, (oma, omac)) = xml.match(node, (xml.omt("OMA"), None))
        if m:
            if len(omac) == 0:
                raise ValueError("No operator given")
            (fun, args) = (omac[0], omac[1:])

            parsed = OMA(term.Term.__parse__(fun), list(map(term.Term.__parse__, args)))
            parsed.metadata = md

            return parsed
        else:
            raise ValueError("Not a well-formed <OMA/>")
