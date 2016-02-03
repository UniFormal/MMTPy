class Backend(object):
    """
    Represents an Abstract Backend to MMT.
    """
    def __init__(self):
        pass

    #
    # DECLARATION
    #
    def getDeclaration(self, pth):
        """
        Gets the declaration of the ContentElement pointed to by pth.
        """

        raise NotImplementedError

    def getDefinition(self, pth):
        """
        Gets the definition of the ContentElement pointed to by pth.
        """

        decl = self.getDeclaration(pth)

        if decl:
            return decl.df
        else:
            return None

    def getType(self, pth):
        """
        Gets the (definitional) type of the ContentElement pointed to by pth.
        """
        decl = self.getDeclaration(pth)

        if decl:
            return decl.tp
        else:
            return None

    #
    # PRESENTATION
    #
    def present(self, tm, presenter="xml"):
        """
        Presents a object (an MMT term) with the specefied presenter.
        """
        raise NotImplementedError

    def presentDeclaration(self, pth, presenter="xml"):
        """
        Presents the declaration of an object with the specefied presenter.
        """
        raise NotImplementedError

    #
    # PARSING
    #

    def parse(self, s, thy):
        """
        Parses a string with respect to a certain theory.
        """

        raise NotImplementedError

    #
    # SIMPLIFICATION
    #
    def simplify(self, obj, thy):
        """
        Simplifies an object with respect to a certain theory.
        """

        raise NotImplementedError

    #
    # TYPE INFERENCE
    #

    def infer(self, obj, fnd):
        """
        Infers the type of an object relative to a theory.
        """

        raise NotImplementedError
    
    def analyze(self, obj, thy):
        """
        Reconstructs the type of an object relative to a theory.
        """

        raise NotImplementedError
