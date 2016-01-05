from .. import utils

from . import path
from .. import xml

"""
    This file defines Terms for MMT. 
    
    Abstractly speaking a term is represented as: 
    
    Term = OMA (fun : Term, args : List[Term])
         | OMV (name : LocalName)
         | OMID (path : ContentPath)
         | OMLIT (value : Object )
         | OMATTR (arg : Term, key : OMID, value : Term)
         | OMBINDC (binder : Term, [context: Context], scopes : List[Term])
"""

# TODO: OMFOREIGN

class Term(): 
    @staticmethod
    def parse(node):
        
        # if we are an OMOBJ we need to ignore the first layer
        (m, (omobj, (child,))) = xml.match(node, (xml.omt("OMOBJ"), [xml.omt()]))
        if m:
            return Term.__parseRec__(child)
        return Term.__parseRec__(node)
    
    @staticmethod
    def __parseRec__(node):
        
        # remove the meta data
        Term.__removeMeta__(node)
        
        # In case of an OMS 
        (m, oms) = xml.match(node, xml.omt("OMS"))
        if m:
            return Term.__parseOMS__(node)
        
        # in case of a something else
    
    @staticmethod
    def __parseOMS__(node):
        (m, oms) = xml.match(node, xml.omt("OMS"))
        if m:
            pth = path.Path.parseBest((node.attrib.get("base"), node.attrib.get("module"), node.attrib.get("name"), ""), isSplit=True)
            return OMID(pth)
        else:
            raise ValueError("not a well-formed idenitifer")
            
    @staticmethod
    def __removeMeta__(node):
        for c in node:
            (m, md) = xml.match(node, "metadata")
            if m:
                node.remove()
        
        

class OMA(utils.caseClass("OMA", Term, [Term]), Term):
    def __init__(self, fun, args):
        super(OMA, self).__init__(fun, args)
        self.fun = fun
        self.args = args

class OMV(utils.caseClass("OMV", path.LocalName), Term):
    def __init__(self, name):
        super(OMV, self).__init__(name)
        self.name = name

class OMID(utils.caseClass("OMID", path.ContentPath), Term):
    def __init__(self, path):
        super(OMID, self).__init__(path)
        self.path = path
    def toXML(self):
        path = self.path
        module = path.module
        base = module.parent
        
        return xml.make_element(xml.omt("OMS"), base=str(base), module=str(module.name), name=str(path.name))

class OMLIT(utils.caseClass("OMLIT", object), Term):
    def __init__(self, value):
        super(OMLIT, self).__init__(value)
        self.value = value

class OMATTR(utils.caseClass("OMATTR", Term, OMID, Term), Term):
    def __init__(self, arg, key, value):
        super(OMATTR, self).__init__(arg, key, value)
        self.value = value

class OMBINDC(utils.caseClass("OMBINDC", Term, [Term]), Term):
    def __init__(self, binder, scopes):
        super(OMBINDC, self).__init__(binder, scopes)
        self.binder = binder
        self.scopes = scopes