from MMTPy import xml, metadata

from MMTPy.objects import path
from MMTPy.caseclass import caseclass
from MMTPy.declarations import declaration

class Theory(caseclass.make(path.DPath, path.LocalName, (path.MPath,), [declaration.Declaration]), declaration.Declaration):
    def __init__(self, base, name, meta, decls):
        super(Theory, self).__init__(base, name, meta, decls)
        self.__initmd__()

        self.base = base
        self.name = name
        self.meta = meta
        self.decls = decls

    def map(self, fn):
        tpds = map(lambda d:d.map(fn), self.decls)

        return fn(Theory(self.base, self.name, self.meta, list(tpds)))

    def toXML(self):
        attrs = {
            "base": self.base,
            "name": self.name
        }

        if self.meta != None:
            attrs["meta"] = self.meta

        return xml.make_element("theory", self.toMetaDataXML(), *map(lambda d:d.toXML(), self.decls), **attrs)

    @staticmethod
    def fromXML(onode):
        (md, node) = metadata.MetaData.extractMetaDataXML(onode)

        if xml.matches(node, "theory"):
            base = path.Path.parseD(node.attrib.get("base"))
            name = path.LocalName.parse(node.attrib.get("name"))

            if "meta" in node.attrib:
                meta = path.Path.parseM(node.attrib.get("meta"))
            else:
                meta = None

            decls = []

            for c in node:
                try:
                    decls.append(declaration.Declaration.fromXML(c))
                except ValueError:
                    pass

            parsed = Theory(base, name, meta, decls)
            parsed.metadata = md

            return parsed
        else:
            raise ValueError("not a well-formed theory")
