from MMTPy import xml, metadata

from MMTPy.paths import path
from MMTPy.clsutils import caseclass, types
from MMTPy.content.structural.content.declarations import declaration
from MMTPy.content.objects.terms import term

@caseclass.caseclass
@types.argtypes(path.LocalName, path.MPath, bool, [declaration.Declaration])
class DeclaredStructure(Structure):
    def __init__(self, name, frm, isImplicit, decls):
        super(DeclaredStructure, self).__init__()

        self.name = name
        self.frm = frm
        self.isImplicit = isImplicit
        self.decls = decls
    def map(self, fn):
        return fn(DefinedStructure(self.frm, self.isImplicit, self.frm, [d.map(fn) for d in self.decls]))
    def toXML(self):
        return xml.make_element("import", self.toMetaDataXML(), *[d.toXML() for d in self.decls], **{"name": self.name, "from": self.frm, "implicit": "true" if self.isImplicit else "false"})

@caseclass.caseclass
@types.argtypes(path.LocalName, path.MPath, bool, term.Term)
class DefinedStructure(Structure):
    def __init__(self, name, frm, isImplicit, df):
        super(DefinedStructure, self).__init__()

        self.name = name
        self.frm = frm
        self.isImplicit = isImplicit
        self.df = df
    def map(self, fn):
        return fn(DefinedStructure(self.frm, self.isImplicit, self.frm, self.df.map(fn)))
    def toXML(self):
        return xml.make_element("import", self.toMetaDataXML(), ("definition", self.df.toXML()), **{"name": self.name, "from": self.frm, "implicit": "true" if self.isImplicit else "false"})

class Structure(declaration.Declaration):
    @staticmethod
    def fromXML(onode):
        (md, node) = metadata.MetaData.extractMetaDataXML(onode)
        if xml.matches(node, "import"):

            name = path.LocalName.parse(node.attrib.get("name"))
            frm = path.Path.parseM(node.attrib.get("from"))
            isImplicit = node.attrib.get("implicit") == "true"

            if xml.matches(node, ("import", ("definition"))):
                parsed = DefinedStructure(name, frm, isImplicit, term.Term.fromXML(node[0][0]))
            else:
                parsed = DeclaredStructure(name, frm, isImplicit, [declaration.Declaration.fromXML(n) for n in node]))



            parsed.metadata = md

            return parsed
        else:
            raise ValueError("not a well-formed structure (or unsupported import)")
