from MMTPy import xml, metadata
from MMTPy.caseclass import caseclass
from MMTPy.objects import obj, path
from MMTPy.objects.terms import term

class VarDecl(caseclass.make(path.LocalName, (term.Term,), (term.Term,), type(None)), obj.Obj):
    def __init__(self, name, tp, df, nt):
        super(VarDecl, self).__init__(name, tp, df, nt)
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

        return xml.make_element(xml.omt("OMV"), self.toMetaDataXML(), *nodes, name=self.name)

    @staticmethod
    def fromXML(onode):
        (md, node) = metadata.MetaData.extractMetaDataXML(onode)
        (m, omv) = xml.match(node, xml.omt("OMV"))
        if m:
            name = path.LocalName.parse(omv.attrib.get("name"))

            tp_node = omv.find("type")

            if tp_node != None:
                tp = term.Term.fromXML(list(tp_node)[0])
            else:
                tp = None

            df_node = omv.find("definition")

            if df_node != None:
                df = term.Term.fromXML(list(df_node)[0])
            else:
                df = None

            parsed = VarDecl(name, tp, df, None)
            parsed.metadata = md

            return parsed
        else:
            raise ValueError("Not a well-formed variable declaration")

class Context(caseclass.make([VarDecl]), obj.Obj):
    def __init__(self, variables):
        super(Context, self).__init__(variables)
        self.variables = variables
    def toXML(self):
        return xml.make_element(xml.omt("OMBVAR"), self.toMetaDataXML(), *map(lambda v:v.toXML(), variables))

    @staticmethod
    def fromXML(onode):
        (md, node) = metadata.MetaData.extractMetaDataXML(onode)

        (m, (omv, decls)) = xml.match(node, (xml.omt("OMBVAR"), None))
        if m:
            parsed = Context(list(map(VarDecl.fromXML, decls)))
            parsed.metadata = md

            return parsed
        else:
            raise ValueError("Not a well-formed context")
