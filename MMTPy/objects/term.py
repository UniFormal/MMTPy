from .. import utils

from . import path

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

class Term(): pass

class OMA(utils.caseClass("OMA", Term, [Term]), Term):
    def __init__(self, fun, args):
        super(OMA, self).__init__(fun, args)
        self.fun = fun
        self.args = args

class OMV(utils.caseClass("OMV", LocalName), Term):
    def __init__(self, name):
        super(OMV, self).__init__(name)
        self.name = name

class OMID(utils.caseClass("OMID", path.ContentPath), Term):
    def __init__(self, path):
        super(OMID, self).__init__(path)
        self.path = path

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