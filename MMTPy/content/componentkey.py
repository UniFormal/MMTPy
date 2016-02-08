from MMTPy.clsutils import caseclass, types

class ComponentKey(object):
    def __init__(self, s):
        self.s = s
    @staticmethod
    def parse(s):
        if s != "" and s in __classmap__:
            return __classmap__[s]()
        elif s.startswith("ext-"):
            return OtherComponent(s)
        else:
            raise ValueError("Invalid name of declaration component")

@caseclass.caseclass
@types.argtypes(types.strtype)
class OtherComponent(ComponentKey):
    def __init__(self, s):
        super(OtherComponent, self).__init__(s)

@caseclass.caseclass
@types.argtypes()
class TypeComponent(ComponentKey):
    def __init__(self):
        super(TypeComponent, self).__init__("type")

@caseclass.caseclass
@types.argtypes()
class DefComponent(ComponentKey):
    def __init__(self):
        super(DefComponent, self).__init__("definition")

@caseclass.caseclass
@types.argtypes()
class DomComponent(ComponentKey):
    def __init__(self):
        super(DomComponent, self).__init__("domain")

@caseclass.caseclass
@types.argtypes()
class CodComponent(ComponentKey):
    def __init__(self):
        super(CodComponent, self).__init__("codomain")

@caseclass.caseclass
@types.argtypes()
class ParamsComponent(ComponentKey):
    def __init__(self):
        super(ParamsComponent, self).__init__("params")

@caseclass.caseclass
@types.argtypes()
class PatternBodyComponent(ComponentKey):
    def __init__(self):
        super(PatternBodyComponent, self).__init__("pattern-body")

@caseclass.caseclass
@types.argtypes()
class MetaDataComponent(ComponentKey):
    def __init__(self):
        super(MetaDataComponent, self).__init__("metadata")

__classmap__ = {
    "type": TypeComponent,
    "definition": DefComponent,
    "domain": DomComponent,
    "codomain": CodComponent,
    "params": ParamsComponent,
    "pattern-body": PatternBodyComponent,
    "metadata": MetaDataComponent
}
