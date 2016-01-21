from MMTPy.caseclass import caseclass, types

class ComponentKey(object):
    @staticmethod
    def parse(s):
        if s != "" and s in __classmap__:
            return __classmap__[s]()
        elif s.startswith("ext-"):
            return OtherComponent(s)
        else:
            raise ValueError("Invalid name of declaration component")

class OtherComponent(caseclass.make(types.strtype), ComponentKey):
    def __init__(self, s):
        super(OtherComponent, self).__init__()
        self.s = s   
            
class TypeComponent(caseclass.make(), ComponentKey):
    def __init__(self):
        super(TypeComponent, self).__init__()
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k

class DefComponent(caseclass.make(), ComponentKey):
    def __init__(self):
        super(DefComponent, self).__init__()
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k
class DomComponent(caseclass.make(), ComponentKey):
    def __init__(self):
        super(DomComponent, self).__init__()
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k
class CodComponent(caseclass.make(), ComponentKey):
    def __init__(self):
        super(CodComponent, self).__init__()
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k
class ParamsComponent(caseclass.make(), ComponentKey):
    def __init__(self):
        super(ParamsComponent, self).__init__()
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k
class PatternBodyComponent(caseclass.make(), ComponentKey):
    def __init__(self):
        super(PatternBodyComponent, self).__init__()
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k
class MetaDataComponent(caseclass.make(), ComponentKey):
    def __init__(self):
        super(MetaDataComponent, self).__init__()
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k
__classmap__ = {
    "type": TypeComponent,
    "definition": DefComponent, 
    "domain": DomComponent,
    "codomain": CodComponent,
    "params": ParamsComponent,
    "pattern-body": PatternBodyComponent,
    "metadata": MetaDataComponent
}