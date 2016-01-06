from MMTPy import utils
from MMTPy import xml

from MMTPy.objects import Object
from MMTPy.objects import term
from MMTPy.objects import path

class VarDecl(utils.caseClass("VarDecl", path.LocalName, (term.Term,), (term.Term,), type(None)), Object):
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
    def fromXML(node):
        md = self.parseMetaDataXML()
        (m, omv) = xml.match(node, xml.omt("OMV"))
        if m:
            name = path.LocalName.parse(omv.attrib.get("name"))
            
            tp_node = omv.find("type")
            
            if tp_node:
                tp = term.Term.fromXML(list(tp_node)[0])
            else:
                tp = None
            
            df_node = omv.find("definition")
            
            if df_node:
                df = term.Term.fromXML(list(df_node)[0])
            
            parsed = VarDecl(name, tp, df, None)
            parsed.metadata = md
            
            return parsed
        else:
            raise ValueError("Not a well-formed variable declaration")

class Context(utils.caseClass("Context", [VarDecl]), Object):
    def __init__(self, variables):
        super(Context, self).__init__(variables)
        self.variables = variables