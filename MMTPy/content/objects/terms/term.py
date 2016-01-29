from MMTPy import xml

from MMTPy.objects import obj

class Term(obj.Obj):
    def __init__(self):
        super(Term, self).__init__()

    def map(self, fn):
        """
        Applies a function to each subcomponent of this term in a depth-first
        approach
        """
        raise NotImplementedError
    def __iter__(self):
        """
        Iterates over all subterms of this term in a depth first manner
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
        # if we are an OMOBJ we need to ignore the first layer
        (m, (omobj, (child,))) = xml.match(node, (xml.omt("OMOBJ"), [xml.omt()]))
        if m:
            return Term.__parse__(child)
        return Term.__parse__(node)

    @staticmethod
    def __parse__(node):
        # in case of OMV
        (m, omv) = xml.match(node, xml.omt("OMV"))
        if m:
            from MMTPy.content.objects.terms import omv
            return omv.OMV.fromXML(node)

        # In case of an OMID
        (m, oms) = xml.match(node, xml.omt("OMS"))
        if m:
            from MMTPy.content.objects.terms import omid
            return omid.OMID.fromXML(node)

        # In case of an OMA
        (m, oma) = xml.match(node, xml.omt("OMA"))
        if m:
            from MMTPy.content.objects.terms import oma
            return oma.OMA.fromXML(node)

        # in case of OMATTR
        (m, omattr) = xml.match(node, xml.omt("OMATTR"))
        if m:
            from MMTPy.content.objects.terms import omattr
            return omattr.OMATTR.fromXML(node)

        # in case of OMBINDC
        (m, ombindc) = xml.match(node, xml.omt("OMBIND"))
        if m:
            from MMTPy.content.objects.terms import ombindc
            return ombindc.OMBINDC.fromXML(node)

        # in case of OMLIT
        (m, omlit) = xml.match(node, xml.omt("OMLIT"))
        if m:
            from MMTPy.content.objects.terms import omlit
            return omlit.UnknownOMLIT.fromXML(node)

        # in case of an OML
        (m, oml) = xml.match(node, xml.omt("OML"))
        if m:
            from MMTPy.content.objects.terms import oml
            return oml.OML.fromXML(node)

        raise ValueError("Either not a well-formed term or unsupported")
