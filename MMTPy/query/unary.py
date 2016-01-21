from MMTPy.caseclass import caseclass, types

class Unary(object):
    @staticmethod
    def parse(s):
        if s != "" and s in __classmap__:
            return __classmap__[s]()
        else:
            return CustomUnary(s)

class CustomUnary(caseclass.make(types.strtype), Unary):
    def __init__(self, s):
        super(CustomUnary, self).__init__(s)
        self.s = s
            
class IsDocument(caseclass.make(), Unary):
    def __init__(self):
        super(IsDocument, self).__init__()
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k
class IsTheory(caseclass.make(), Unary):
    def __init__(self):
        super(IsTheory, self).__init__()
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k
class isView(caseclass.make(), Unary):
    def __init__(self):
        super(isView, self).__init__()
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k
class isStyle(caseclass.make(), Unary):
    def __init__(self):
        super(isStyle, self).__init__()
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k
class IsStructure(caseclass.make(), Unary):
    def __init__(self):
        super(IsStructure, self).__init__()
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k
class IsConstant(caseclass.make(), Unary):
    def __init__(self):
        super(IsConstant, self).__init__()
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k
class IsPattern(caseclass.make(), Unary):
    def __init__(self):
        super(IsPattern, self).__init__()
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k
class IsInstance(caseclass.make(), Unary):
    def __init__(self):
        super(IsInstance, self).__init__()
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k
class IsConAss(caseclass.make(), Unary):
    def __init__(self):
        super(IsConAss, self).__init__()
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k
class IsStrAss(caseclass.make(), Unary):
    def __init__(self):
        super(IsStrAss, self).__init__()
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k
class IsNotation(caseclass.make(), Unary):
    def __init__(self):
        super(IsNotation, self).__init__()
        
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