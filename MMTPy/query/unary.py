from MMTPy.clsutils import caseclass, types

class Unary(object):
    def __init__(self):
        pass
    @staticmethod
    def parse(s):
        if s != "" and s in __classmap__:
            return __classmap__[s]()
        else:
            return CustomUnary(s)

@caseclass.caseclass
@types.argtypes(types.strtype)
class CustomUnary(Unary):
    def __init__(self, s):
        Unary.__init__(self)
        
        self.s = s

@caseclass.caseclass
@types.argtypes()
class IsDocument(Unary):
    def __init__(self):
        Unary.__init__(self)
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k

@caseclass.caseclass
@types.argtypes()
class IsTheory(Unary):
    def __init__(self):
        Unary.__init__(self)
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k
@caseclass.caseclass
@types.argtypes()
class isView(Unary):
    def __init__(self):
        Unary.__init__(self)
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k

@caseclass.caseclass
@types.argtypes()
class isStyle(Unary):
    def __init__(self):
        Unary.__init__(self)
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k

@caseclass.caseclass
@types.argtypes()
class IsStructure(Unary):
    def __init__(self):
        Unary.__init__(self)
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k

@caseclass.caseclass
@types.argtypes()
class IsConstant(Unary):
    def __init__(self):
        Unary.__init__(self)
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k

@caseclass.caseclass
@types.argtypes()
class IsPattern(Unary):
    def __init__(self):
        Unary.__init__(self)
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k

@caseclass.caseclass
@types.argtypes()
class IsInstance(Unary):
    def __init__(self):
        Unary.__init__(self)
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k

@caseclass.caseclass
@types.argtypes()
class IsConAss(Unary):
    def __init__(self):
        Unary.__init__(self)
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k

@caseclass.caseclass
@types.argtypes()
class IsStrAss(Unary):
    def __init__(self):
        Unary.__init__(self)
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k

@caseclass.caseclass
@types.argtypes()
class IsNotation(Unary):
    def __init__(self):
        Unary.__init__(self)
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k
__classmap__ = {
    "document": IsDocument, 
    "theory": IsTheory, 
    "view": isView, 
    "style": isStyle, 
    "structure": IsStructure, 
    "constant": IsConstant, 
    "pattern": IsPattern, 
    "instance": IsInstance, 
    "conass": IsConAss, 
    "strass": IsStrAss,
    "notation": IsNotation
}