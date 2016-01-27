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
        return oma.OMA(self, *args)
    def uninit(self):
        """
        Returns the list of arguments used to construct this Term. See the
        specific implementations for details of the return times.
        """
        return self.__uninit__()
