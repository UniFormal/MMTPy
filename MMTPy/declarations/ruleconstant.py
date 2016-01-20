from MMTPy.declarations import declaration
from MMTPy.objects import path

from MMTPy import metadata
from MMTPy import xml
from MMTPy.caseclass import caseclass

class RuleConstant(caseclass.make(path.LocalName), declaration.Declaration):
    def __init__(self, name):
        super(RuleConstant, self).__init__(name)
        self.__initmd__()

        self.name = name

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
