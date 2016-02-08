from MMTPy import metadata
from MMTPy import xml

class Obj(metadata.MetaData):
    def toOBJXML(self):
        nowrapnode = self.toXML()
        return xml.make_element(xml.omt("OMOBJ"), nowrapnode)
    @staticmethod
    def fromXML(node):
        """
        Parses an XML node into an Obj
        """
        # an OMV can either be a context or an OMV term
        if xml.matches(node, xml.omt("OMV")):
            try:
                from MMTPy.content.objects import vardecl
                return vardecl.VarDecl.fromXML(node)
            except ValueError:
                from MMTPy.content.objects.terms import omv
                return omv.OMV.fromXML(node)

        # an OMBVAR represents a context
        elif xml.matches(node, xml.omt("OMBVAR")):
            from MMTPy.content.objects import context
            return context.Context.fromXML(node)

        # everything else is a term
        else:
            from MMTPy.content.objects.terms import term
            return term.Term.fromXML(node)
