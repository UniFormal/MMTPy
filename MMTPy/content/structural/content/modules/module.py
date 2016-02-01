from MMTPy.content.structural.content import contentelement
from MMTPy import xml

class Module(contentelement.ContentElement):
    """
    Represents an MMT module
    """

    @staticmethod
    def fromXML(node):
        if xml.matches(node, "view"):
            from MMTPy.content.structural.content.modules import view
            return view.View.fromXML(node)
        elif xml.matches(node, "theory"):
            from MMTPy.content.structural.content.modules import theory
            return theory.Theory.fromXML(node)
