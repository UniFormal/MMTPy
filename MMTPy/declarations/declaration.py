from MMTPy import xml

from MMTPy.objects import obj
from MMTPy import metadata


class Declaration(metadata.MetaData):
    def __init__(self):
        super(Declaration, self).__init__()
    @staticmethod
    def fromXML(node):

        # in case of a theory
        if xml.matches(node, "theory"):
            from MMTPy.declarations import theory
            return theory.Theory.fromXML(node)

        # in case of a view
        if xml.matches(node, "view"):
            from MMTPy.declarations import view
            return view.View.fromXML(node)

        # in case of an import
        if xml.matches(node, "import"):
            from MMTPy.declarations import structure
            return structure.Structure.fromXML(node)

        # in case of a constant
        if xml.matches(node, "constant"):
            from MMTPy.declarations import constant
            return constant.Constant.fromXML(node)

        raise ValueError("Not a well-formed declaration")
