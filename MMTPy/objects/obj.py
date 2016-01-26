from MMTPy import metadata
from MMTPy import xml

class Obj(metadata.MetaData):
    def __init__(self):
        super(Obj, self).__init__()
    def toOBJXML(self):
        nowrapnode = self.toXML()
        return xml.make_element(xml.omt("OMOBJ"), nowrapnode)
    @staticmethod
    def fromXML(node):
        from MMTPy.objects.terms import term
        return term.Term.fromXML(node)
    def __call__(self, *args, **kwargs):
        """
        Applies this term to a list of other terms. Equivalent to
        oma.OMA(self, *args).
        """

        from MMTPy.objects.terms import oma

        if "lf" in kwargs and kwargs["lf"]:
            from MMTPy.objects import path
            lf_apply = path.Path.parse("http://cds.omdoc.org/urtheories?LF?apply")
            return lf_apply(self, *args)

        return oma.OMA(self, *args)
    def uncall(self):
        """
        Returns the arguments given to this term.
        """
        return self.__uninit__()
    def toTerm(self):
        return self
    def __invert__(self):
        """
        Alias of toTerm(self)
        """
        return self.toTerm()
