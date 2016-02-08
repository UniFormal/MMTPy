from MMTPy import xml, metadata

from MMTPy.paths import path
from MMTPy.clsutils import caseclass, types
from MMTPy.content.structural.content.declarations import declaration

@caseclass.caseclass
@types.argtypes(path.LocalName)
class RuleConstant(declaration.Declaration):
    def __init__(self, name):
        super(RuleConstant, self).__init__()

        self.name = name
    def map(self, fn):
        return fn(RuleConstant(self.name))

    def toXML(self):
        return xml.make_element("ruleconstant", self.toMetaDataXML(), **{"name": self.name})

    @staticmethod
    def fromXML(onode):
        (md, node) = metadata.MetaData.extractMetaDataXML(onode)
        if xml.matches(node, "ruleconstant"):

            parsed = RuleConstant(path.LocalName.parse(node.attrib.get("name")))
            parsed.metadata = md

            return parsed
        else:
            raise ValueError("not a well-understood ruleconstant")
