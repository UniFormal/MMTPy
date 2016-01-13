from MMTPy import utils
from MMTPy.objects import context
from MMTPy import metadata

from MMTPy.objects import path
from MMTPy.objects import term
from MMTPy import xml

from MMTPy.declarations import declaration

class Constant(utils.caseClass("Constant", path.LocalName, (term.Term,), (term.Term,), type(None)), declaration.Declaration):
    def __init__(self, name, tp, df, nt):
        super(Constant, self).__init__(name, tp, df, nt)
        self.__initmd__()

        self.name = name
        self.tp = tp
        self.df = df
        self.nt = nt
    def toXML(self):
        nodes = []

        if self.tp:
            nodes += [xml.make_element("type", self.tp.toXML())]
        if self.df:
            nodes += [xml.make_element("definition", self.df.toXML())]

        return xml.make_element("constant", self.toMetaDataXML(), *nodes, name=self.name)

    @staticmethod
    def fromXML(onode):
        (md, node) = metadata.MetaData.parseMetaDataXML(onode)
        (m, cst) = xml.match(node, "constant")
        if m:
            name = path.LocalName.parse(cst.attrib.get("name"))

            tp_node = cst.find("type")

            if tp_node:
                tp = term.Term.fromXML(list(tp_node)[0])
            else:
                tp = None

            df_node = cst.find("definition")

            if df_node:
                df = term.Term.fromXML(list(df_node)[0])
            else:
                df = None

            parsed = Constant(name, tp, df, None)
            parsed.metadata = md

            return parsed
        else:
            raise ValueError("Not a well-formed constant declaration")
