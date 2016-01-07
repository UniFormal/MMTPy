from MMTPy import utils

from MMTPy.objects import Object
from MMTPy.objects import path
from MMTPy import xml

"""
    This file defines Terms for MMT.

    Abstractly speaking a term is represented as:

    Term = OMV (name : LocalName)
         | OMID (path : ContentPath)
         | OMA (fun : Term, args : List[Term])
         | OMATTR (arg : Term, key : OMID, value : Term)
         | OMBINDC (binder : Term, [context: Context], scopes : List[Term])
"""
# TODO: OMLIT, OMFOREIGN

class Term(Object):
    def __init__(self):
        super(Term, self).__init__()

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
            return OMV.fromXML(node)

        # In case of an OMID
        (m, oms) = xml.match(node, xml.omt("OMS"))
        if m:
            return OMID.fromXML(node)

        # In case of an OMA
        (m, oma) = xml.match(node, xml.omt("OMA"))
        if m:
            return OMA.fromXML(node)

        (m, omattr) = xml.match(node, xml.omt("OMATTR"))
        if m:
            return OMATTR.fromXML(node)

class OMV(utils.caseClass("OMV", path.LocalName), Term):
    def __init__(self, name):
        super(OMV, self).__init__(name)
        self.name = name
    def toXML(self):
        return xml.make_element(xml.omt("OMV"), self.toMetaDataXML(), name=self.name)

    @staticmethod
    def fromXML(node):
        md = Object.parseMetaDataXML(node)
        (m, omv) = xml.match(node, xml.omt("OMV"))
        if m:
            pth = path.LocalName.parse(node.attrib.get("name"))

            parsed = OMV(pth)
            parsed.metadata = md

            return parsed
        else:
            raise ValueError("not a well-formed value")

class OMID(utils.caseClass("OMID", path.ContentPath), Term):
    def __init__(self, path):
        super(OMID, self).__init__(path)
        self.path = path
    def toXML(self):
        return xml.make_element(xml.omt("OMS"), self.toMetaDataXML(), base=self.path.module.parent, module=self.path.module.name, name=self.path.name)

    @staticmethod
    def fromXML(node):
        md = Object.parseMetaDataXML(node)
        (m, oms) = xml.match(node, xml.omt("OMS"))
        if m:
            pth = path.Path.parseBest((node.attrib.get("base"), node.attrib.get("module"), node.attrib.get("name"), ""), isSplit=True)

            parsed = OMID(pth)
            parsed.metadata = md

            return parsed
        else:
            raise ValueError("not a well-formed idenitifer")

class OMA(utils.caseClass("OMA", Term, [Term]), Term):
    def __init__(self, fun, args):
        super(OMA, self).__init__(fun, args)
        self.fun = fun
        self.args = args
    def toXML(self):
        return xml.make_element(xml.omt("OMA"), self.toMetaDataXML(), self.fun.toXML(), *map(lambda a:a.toXML(), self.args))

    @staticmethod
    def fromXML(node):
        md = Object.parseMetaDataXML(node)
        (m, (oma, omac)) = xml.match(node, (xml.omt("OMA"), None))
        if m:
            if len(omac) == 0:
                raise ValueError("No operator given")
                (fun, args) = (omac[0], omac[1:])

            parsed = OMA(Term.__parse__(fun), list(map(Term.__parse__, args)))
            parsed.metadata = md

            return parsed
        else:
            raise ValueError("not a well-formed application")

class OMATTR(utils.caseClass("OMATTR", Term, OMID, Term), Term):
    def __init__(self, arg, key, value):
        super(OMATTR, self).__init__(arg, key, value)
        self.arg = arg
        self.key = key
        self.value = value
    def toXML(self):
        return xml.make_element(xml.omt("OMATTR"),
            self.toMetaDataXML(),
            (xml.omt("OMATP"), [self.key.toXML(), self.value.toXML()]),
            self.arg.toXML()
        )

    @staticmethod
    def fromXML(node):
        md = Object.parseMetaDataXML(node)
        (m, (omattr, (omatp, (omkey, omval), omarg))) = xml.match(node,
            (xml.omt("OMATTR"),
                [
                    (xml.omt("OMATP"), [xml.omt(""), xml.omt("")]),
                    xml.omt("")
                ]
            )
        )

        if m:
            parsed = OMATTR(Term.__parse__(omarg), Term.__parse__(omkey), Term.__parse__(omval))
            parsed.metadata = md

            return parsed
        else:
            raise ValueError("Malformed <OMATTR>")

from MMTPy.objects import context
class OMBINDC(utils.caseClass("OMBINDC", Term, context.Context, [Term]), Term):
    def __init__(self, binder, ctx, scopes):
        super(OMBINDC, self).__init__(binder, scopes)
        self.binder = binder
        self.ctx = ctx
        self.scopes = scopes
