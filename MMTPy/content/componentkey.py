from MMTPy.clsutils import caseclass, types

class ComponentKey(object):
    def __init__(self):
        pass
    
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
        ComponentKey.__init__(self)
        
        self.s = s   

@caseclass.caseclass
@types.argtypes()
class TypeComponent(ComponentKey):
    def __init__(self):
        ComponentKey.__init__(self)
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k

@caseclass.caseclass
@types.argtypes()
class DefComponent(ComponentKey):
    def __init__(self):
        ComponentKey.__init__(self)
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k

@caseclass.caseclass
@types.argtypes()
class DomComponent(ComponentKey):
    def __init__(self):
        ComponentKey.__init__(self)
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k

@caseclass.caseclass
@types.argtypes()
class CodComponent(ComponentKey):
    def __init__(self):
        ComponentKey.__init__(self)
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k

@caseclass.caseclass
@types.argtypes()
class ParamsComponent(ComponentKey):
    def __init__(self):
        ComponentKey.__init__(self)
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k

@caseclass.caseclass
@types.argtypes()
class PatternBodyComponent(ComponentKey):
    def __init__(self):
        ComponentKey.__init__(self)
        
        for (k, v) in __classmap__.items():
            if v == self.__class__:
                self.s = k

@caseclass.caseclass
@types.argtypes()
class MetaDataComponent(ComponentKey):
    def __init__(self):
        ComponentKey.__init__(self)
        
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