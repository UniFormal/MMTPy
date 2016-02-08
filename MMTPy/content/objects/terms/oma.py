from MMTPy import xml, metadata

from MMTPy.paths import path
from MMTPy.clsutils import caseclass, types
from MMTPy.content.objects.terms import term

@caseclass.caseclass
@types.argtypes(term.Term, [term.Term])
class OMA(term.Term):
    """
    An OMA represents an application of a list of terms on another term
    """
    def __init__(self, fun, args):
        super(OMA, self).__init__()

        self.fun = fun
        self.args = list(args)
    def uncall(self, **kwargs):
        """
        Unpacks an object into its construction parameters
        """

        if "lf" in kwargs and kwargs["lf"]:
            from MMTPy.library.lf import wrappers
            return wrappers.lf_unapply(tm)

        return (self.fun, self.args)
    def map(self, fn):
        f = self.fun.map(fn)
        a = list(map(lambda s:s.map(fn), self.args))

        return fn(OMA(f, a))

    def toXML(self):
        return xml.make_element(xml.omt("OMA"), self.toMetaDataXML(), self.fun.toXML(), list(map(lambda a:a.toXML(), self.args)))

    @staticmethod
    def fromXML(onode):
        (md, node) = metadata.MetaData.extractMetaDataXML(onode)
        (m, (oma, omac)) = xml.match(node, (xml.omt("OMA"), None))
        if m:
            if len(omac) == 0:
                raise ValueError("No operator given")
            (fun, args) = (omac[0], omac[1:])

            parsed = OMA(term.Term.__parse__(fun), list(map(term.Term.__parse__, args)))
            parsed.metadata = md

            return parsed
        else:
            raise ValueError("Not a well-formed <OMA/>")
