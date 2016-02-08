from MMTPy import xml, metadata

from MMTPy.content.structural.content import contentelement


class Declaration(contentelement.ContentElement):
    def __init__(self):
        super(Declaration, self).__init__()

        self.decls = []
    def map(self, fn):
        """
        Applies a function to each subcomponent of this VarDecl in a depth-first
        approach
        """

        raise NotImplementedError
    def getConstantDeclaration(self, ln):
        """
        Gets a constant declaration of the specific name
        """

        from MMTPy.content.structural.content.declarations import constant

        for d in self.decls:
            if isinstance(d, constant.Constant):
                if d.name == ln:
                    return d

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

        # in case of an import
        if xml.matches(node, "import"):
            from MMTPy.content.structural.content.declarations import structure
            return structure.Structure.fromXML(node)

        # in case of a constant
        if xml.matches(node, "constant"):
            from MMTPy.content.structural.content.declarations import constant
            return constant.Constant.fromXML(node)

        # parse a rule constant
        if xml.matches(node, "ruleconstant"):
            from MMTPy.content.structural.content.declarations import ruleconstant
            return ruleconstant.RuleConstant.fromXML(node)

        raise ValueError("Not a well-formed declaration")
