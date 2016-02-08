from MMTPy.clsutils import caseclass, types

class Unary(object):
    def __init__(self, s):
        self.s = s
    
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
        super(CustomUnary, self).__init__(s)

@caseclass.caseclass
@types.argtypes()
class IsDocument(Unary):
    def __init__(self):
        super(CustomUnary, self).__init__("document")

@caseclass.caseclass
@types.argtypes()
class IsTheory(Unary):
    def __init__(self):
        super(IsTheory, self).__init__("theory")

@caseclass.caseclass
@types.argtypes()
class isView(Unary):
    def __init__(self):
        super(isView, self).__init__("view")

@caseclass.caseclass
@types.argtypes()
class isStyle(Unary):
    def __init__(self):
        super(isStyle, self).__init__("style")

@caseclass.caseclass
@types.argtypes()
class IsStructure(Unary):
    def __init__(self):
        super(IsStructure, self).__init__("structure")

@caseclass.caseclass
@types.argtypes()
class IsConstant(Unary):
    def __init__(self):
        super(IsConstant, self).__init__("constant")

@caseclass.caseclass
@types.argtypes()
class IsPattern(Unary):
    def __init__(self):
        super(IsPattern, self).__init__("pattern")

@caseclass.caseclass
@types.argtypes()
class IsInstance(Unary):
    def __init__(self):
        super(IsInstance, self).__init__("instance")

@caseclass.caseclass
@types.argtypes()
class IsConAss(Unary):
    def __init__(self):
        super(IsConAss, self).__init__("conass")

@caseclass.caseclass
@types.argtypes()
class IsStrAss(Unary):
    def __init__(self):
        super(IsStrAss, self).__init__("strass")

@caseclass.caseclass
@types.argtypes()
class IsNotation(Unary):
    def __init__(self):
        super(IsNotation, self).__init__("notation")

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
