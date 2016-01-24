from MMTPy import xml, metadata

from MMTPy.objects import obj

class Declaration(metadata.MetaData):
    def __init__(self):
        super(Declaration, self).__init__()
    def map(self, fn):
        """
        Applies a function to each subcomponent of this VarDecl in a depth-first
        approach
        """

        raise NotImplementedError

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

        # parse a rule constant
        if xml.matches(node, "ruleconstant"):
            from MMTPy.declarations import ruleconstant
            return ruleconstant.RuleConstant.fromXML(node)

        raise ValueError("Not a well-formed declaration")
