from MMTPy import xml, metadata

from MMTPy.objects import path
from MMTPy.caseclass import caseclass, types
from MMTPy.objects.terms import term, omid

class OMLIT(caseclass.make(term.Term, types.strtype), term.Term):
    def __init__(self, tp, value):
        super(OMLIT, self).__init__(tp, value)
        self.tp = tp
        self.value = value
    def toXML(self):
        attrs = {"value": self.value}
        children = []
        if isinstance(self.tp, omid.OMID):
            attrs["type"] = self.tp.path
        else:
            children = [self.tp.toXML()]

        return xml.make_element(xml.omt("OMLIT"), self.toMetaDataXML(), *children, **attrs)
    @staticmethod
    def fromXML(onode):
        (md, node) = metadata.MetaData.extractMetaDataXML(onode)

        (m, omlit) = xml.match(node, xml.omt("OMLIT"))
        if m:
            value = omlit.attrib.get("value")

            if "type" in omlit.attrib:
                tp = omid.OMID(path.Path.parseBest(omlit.attrib.get("type")))
            else:
                tp = term.Term.fromXML(omlit[0][0])

            parsed = OMLIT(tp, value)
            parsed.metadata = md

            return parsed
        else:
            raise ValueError("Not a well-formed <OMLIT/>")
