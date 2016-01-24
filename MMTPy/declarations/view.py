from MMTPy import xml, metadata

from MMTPy.objects import path
from MMTPy.caseclass import caseclass
from MMTPy.declarations import declaration

class View(caseclass.make(path.DPath, path.LocalName, path.MPath, path.MPath, [declaration.Declaration]), declaration.Declaration):
    def __init__(self, base, name, frm, to, decls):
        super(View, self).__init__(base, name, frm, to, decls)
        self.__initmd__()

        self.frm = frm
        self.to = to

        self.base = base
        self.name = name
        self.decls = decls
    def map(self, fn):
        vds = map(lambda d:d.map(fn), self.decls)

        return fn(View(self.base, self.name, self.frm, self.to, list(vds)))

    def toXML(self):
        attrs = {
            "base": self.base,
            "name": self.name,
            "from": self.frm,
            "to": self.to
        }

        return xml.make_element("view", self.toMetaDataXML(), *map(lambda d:d.toXML(), self.decls), **attrs)

    @staticmethod
    def fromXML(onode):
        (md, node) = metadata.MetaData.extractMetaDataXML(onode)

        if xml.matches(node, "view"):
            base = path.Path.parseD(node.attrib.get("base"))
            name = path.LocalName.parse(node.attrib.get("name"))

            frm = path.Path.parseM(node.attrib.get("from"))
            to  = path.Path.parseM(node.attrib.get("to"))

            decls = []

            for c in node:
                try:
                    decls.append(declaration.Declaration.fromXML(c))
                except ValueError:
                    pass

            parsed = View(base, name, frm, to, decls)
            parsed.metadata = md

            return parsed
        else:
            raise ValueError("not a well-formed view")
