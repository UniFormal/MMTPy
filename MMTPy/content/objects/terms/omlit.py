from MMTPy import xml, metadata

from MMTPy.paths import path
from MMTPy.caseclass import caseclass, types
from MMTPy.content.objects.terms import term, omid

from MMTPy.literals import semantic

class UnknownOMLIT(caseclass.make(term.Term, types.strtype), term.Term):
    def __init__(self, syntp, value):
        super(UnknownOMLIT, self).__init__(syntp, value)
        self.__initmd__()

        self.syntp = syntp
        self.value = value
    def map(self, fn):
        return fn(UnknownOMLIT(self.syntp.map(fn), self.value))
    def toXML(self):
        attrs = {"value": self.value}
        children = []
        if isinstance(self.syntp, omid.OMID):
            attrs["type"] = self.syntp.path
        else:
            children = [xml.make_element("type", self.syntp.toXML())]

        return xml.make_element(xml.omt("OMLIT"), self.toMetaDataXML(), *children, **attrs)
    def toOMLIT(self, semtype):
        o = semtype.fromString(self.value)

        # create the omlit and ransfer meta data
        lit = OMLIT(semtype, self.syntp, o)
        lit.metadata = self.metadata
        
        return lit
    @staticmethod
    def fromXML(onode):
        (md, node) = metadata.MetaData.extractMetaDataXML(onode)

        (m, omlit) = xml.match(node, xml.omt("OMLIT"))
        if m:
            value = omlit.attrib.get("value")

            if "type" in omlit.attrib:
                tp = omid.OMID(path.Path.parse(omlit.attrib.get("type")))
            else:
                tp = term.Term.fromXML(omlit[0][0])

            parsed = UnknownOMLIT(tp, value)
            parsed.metadata = md

            return parsed
        else:
            raise ValueError("Not a well-formed <OMLIT/>")

class OMLIT(caseclass.make(semantic.SemanticType, term.Term, object), UnknownOMLIT):
    def __init__(self, semtp, syntp, o):
        super(OMLIT, self).__init__(semtp, syntp, o)
        self.__initmd__()

        if not semtp.valid(o):
            raise ValueError("SemanticType is not valid for the given object")

        self.o = o
        self.semtp = semtp
        self.syntp = syntp

        self.value = self.semtp.toString(o)

    def map(self, fn):
        return fn(OMLIT(self.semtp, self.syntp.map(fn), obj))

    def __repr__(self):
        return "OMLIT[%s, %r]" % (self.semtp.name, self.o)
