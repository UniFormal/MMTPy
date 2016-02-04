from MMTPy import xml, metadata
from MMTPy.clsutils import caseclass, types
from MMTPy.content.objects import obj
from MMTPy.paths import path
from MMTPy.content.objects.terms import term

@caseclass.caseclass
@types.argtypes(path.LocalName, (term.Term,), (term.Term,), type(None))
class VarDecl(obj.Obj):
    def __init__(self, name, tp, df, nt):
        obj.Obj.__init__(self)
        
        self.name = name
        self.tp = tp
        self.df = df
        self.nt = nt
    def map(self, fn):
        """
        Applies a function to each subcomponent of this VarDecl in a depth-first
        approach
        """

        vtp = self.tp.map(fn) if self.tp != None else None
        vdf = self.df.map(fn) if self.df != None else None

        return fn(VarDecl(self.name, vtp, vdf, self.nt))

    def __iter__(self):
        """
        Iterates over all subcomponents of this VarDecl in a depth first manner
        """
        components = []

        def getitems(x):
            components.append(x)
            return x

        self.map(getitems)

        for c in components:
            yield c
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