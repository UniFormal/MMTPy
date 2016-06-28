from case_class import AbstractCaseClass


class ComponentKey(AbstractCaseClass):
    """ Represents the Key for a single Component. """

    def __init__(self, key):
        """ Creates a new ComponentKey() object.
        :param key: Human-readable component of this ComponentKey.
        :type key: str
        """

        self.__key = key  # type: str

    @property
    def key(self):
        """ Returns the key of this ComponentKey.

        :rtype: str
        """

        return self.__key

    @staticmethod
    def parse(s):
        """Parses a Human Readable representation into a ComponentKey.

        :param s: Representation to parse.
        :type s: str
        :rtype: ComponentKey
        """

        if s != "" and s in __classmap__:
            return __classmap__[s]()
        elif s.startswith("ext-"):
            return OtherComponent(s[len("ext-"):])
        else:
            raise ValueError("Invalid name of declaration component")

    def __str__(self):
        """ Turns this ComponentKey into a string.

        :rtype: str
        """

        return self.key


class OtherComponent(ComponentKey):
    """ A custom component that is not part a ComponentKey. """

    def __init__(self, ext_key):
        """ Creates a new OtherComponent() instance.

        :param ext_key: Key for this OtherComponent.
        :type ext_key: str
        """

        super(OtherComponent, self).__init__("ext-%s" % (ext_key, ))

        self.__ext_key = ext_key  # type: str

    def ext_key(self):
        """ Returns the key for this OtherComponent().

        :rtype: str
        """

        return self.__ext_key


class TypeComponent(ComponentKey):
    """ Represents a type component of a definition. """

    def __init__(self):
        """ Creates a new TypeComponent() instance. """

        super(TypeComponent, self).__init__("type")


class DefComponent(ComponentKey):
    """ Represents a definition component of a definition. """

    def __init__(self):
        """ Creates a new DefComponent() instance. """

        super(DefComponent, self).__init__("definition")


class DomComponent(ComponentKey):
    """ Represents a domain component of a definition. """

    def __init__(self):
        """ Creates a new DomComponent() instance. """

        super(DomComponent, self).__init__("domain")


class CodComponent(ComponentKey):
    """ Represents a co-domain component of a definition. """

    def __init__(self):
        """ Creates a new CodComponent() instance. """

        super(CodComponent, self).__init__("codomain")


class ParamsComponent(ComponentKey):
    """ Represents a parameters component of a definition. """

    def __init__(self):
        """ Creates a new ParamsComponent() instance. """

        super(ParamsComponent, self).__init__("params")


class PatternBodyComponent(ComponentKey):
    """ Represents a pattern-body component of a definition. """

    def __init__(self):
        """ Creates a new PatternBodyComponent() instance. """

        super(PatternBodyComponent, self).__init__("pattern-body")


class MetaDataComponent(ComponentKey):
    """ Represents a meta-data component of a definition. """

    def __init__(self):
        """ Creates a new MetaDataComponent() instance. """

        super(MetaDataComponent, self).__init__("metadata")

__classmap__ = {
    "type": TypeComponent,
    "definition": DefComponent,
    "domain": DomComponent,
    "codomain": CodComponent,
    "params": ParamsComponent,
    "pattern-body": PatternBodyComponent,
    "metadata": MetaDataComponent
}

__all__ = ["ComponentKey", "TypeComponent", "DefComponent", "DomComponent",
           "CodComponent", "ParamsComponent", "PatternBodyComponent",
           "MetaDataComponent", "OtherComponent"]