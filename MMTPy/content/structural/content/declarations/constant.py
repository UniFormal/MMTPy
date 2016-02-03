from MMTPy import xml, metadata

from MMTPy.paths import path
from MMTPy.content.objects import context
from MMTPy.content.objects.terms import term
from MMTPy.caseclass import caseclass
from MMTPy.content.structural.content.declarations import declaration

class Constant(caseclass.make(path.LocalName, (path.LocalName,), (term.Term,), (term.Term,), type(None)), declaration.Declaration):
    """
    Represents a Constant that is declared in a theory
    """
    def __init__(self, name, alias, tp, df, nt):
        super(Constant, self).__init__(name, alias, tp, df, nt)
        self.__initmd__()

        self.name = name
        self.alias = alias
        self.tp = tp
        self.df = df
        self.nt = nt
    def map(self, fn):
        ctp = self.tp.map(fn) if self.tp != None else None
        cdf = self.df.map(fn) if self.df != None else None

        return fn(Constant(self.name, ctp, cdf, self.nt))
    def toXML(self):
        nodes = []
        attrs = {
            "name": self.name
        }

        if self.tp != None:
            nodes += [xml.make_element("type", self.tp.toXML())]
        if self.df != None:
            nodes += [xml.make_element("definition", self.df.toXML())]
        if self.alias != None:
            attrs["alias"] = self.alias

        return xml.make_element("constant", self.toMetaDataXML(), *nodes, **attrs)

    @staticmethod
    def fromXML(onode):
        (md, node) = metadata.MetaData.extractMetaDataXML(onode)
        (m, cst) = xml.match(node, "constant")
        if m:
            name = path.LocalName.parse(cst.attrib.get("name"))

            tp_node = cst.find("type")

            if tp_node != None:
                tp = term.Term.fromXML(list(tp_node)[0])
            else:
                tp = None

            df_node = cst.find("definition")

            if df_node != None:
                df = term.Term.fromXML(list(df_node)[0])
            else:
                df = None

            if "alias" in cst.attrib:
                alias = cst.attrib.get("alias")
            else:
                alias = None

            parsed = Constant(name, alias, tp, df, None)
            parsed.metadata = md

            return parsed
        else:
            raise ValueError("Not a well-formed constant declaration")
