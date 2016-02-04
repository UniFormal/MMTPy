from MMTPy.clsutils import caseclass, types
# TODO: Figure out custom binary

class Binary(object):
    def __init__(self):
        pass
    
    @staticmethod
    def parse(s):
        for (k, v) in __classmapf__.items():
            if v.__name__ == s:
                return v()
        raise ValueError("Unknown Binary")

@caseclass.caseclass
@types.argtypes()
class DependsOn(Binary):
    def __init__(self):
        Binary.__init__(self)
        
        self.name = self.__class__.__name__
        
        for (k, v) in __classmapf__.items():
            if v == self.__class__:
                self.desc = k
        for (k, v) in __classmapb__.items():
            if v == self.__class__:
                self.backwardsDesc = k

@caseclass.caseclass
@types.argtypes()
class HasMeta(Binary):
    def __init__(self):
        Binary.__init__(self)
        
        self.name = self.__class__.__name__
        
        for (k, v) in __classmapf__.items():
            if v == self.__class__:
                self.desc = k
        for (k, v) in __classmapb__.items():
            if v == self.__class__:
                self.backwardsDesc = k

@caseclass.caseclass
@types.argtypes()
class Includes(Binary):
    def __init__(self):
        Binary.__init__(self)
        
        self.name = self.__class__.__name__
        
        for (k, v) in __classmapf__.items():
            if v == self.__class__:
                self.desc = k
        for (k, v) in __classmapb__.items():
            if v == self.__class__:
                self.backwardsDesc = k

@caseclass.caseclass
@types.argtypes()
class HasDomain(Binary):
    def __init__(self):
        Binary.__init__(self)
        
        self.name = self.__class__.__name__
        
        for (k, v) in __classmapf__.items():
            if v == self.__class__:
                self.desc = k
        for (k, v) in __classmapb__.items():
            if v == self.__class__:
                self.backwardsDesc = k

@caseclass.caseclass
@types.argtypes()
class HasCodomain(Binary):
    def __init__(self):
        Binary.__init__(self)
        
        self.name = self.__class__.__name__
        
        for (k, v) in __classmapf__.items():
            if v == self.__class__:
                self.desc = k
        for (k, v) in __classmapb__.items():
            if v == self.__class__:
                self.backwardsDesc = k

@caseclass.caseclass
@types.argtypes()
class IsInstanceOf(Binary):
    def __init__(self):
        Binary.__init__(self)
        
        self.name = self.__class__.__name__
        
        for (k, v) in __classmapf__.items():
            if v == self.__class__:
                self.desc = k
        for (k, v) in __classmapb__.items():
            if v == self.__class__:
                self.backwardsDesc = k

@caseclass.caseclass
@types.argtypes()
class RefersTo(Binary):
    def __init__(self):
        Binary.__init__(self)
        
        self.name = self.__class__.__name__
        
        for (k, v) in __classmapf__.items():
            if v == self.__class__:
                self.desc = k
        for (k, v) in __classmapb__.items():
            if v == self.__class__:
                self.backwardsDesc = k

@caseclass.caseclass
@types.argtypes()
class Declares(Binary):
    def __init__(self):
        Binary.__init__(self)
        
        self.name = self.__class__.__name__
        
        for (k, v) in __classmapf__.items():
            if v == self.__class__:
                self.desc = k
        for (k, v) in __classmapb__.items():
            if v == self.__class__:
                self.backwardsDesc = k

@caseclass.caseclass
@types.argtypes()
class IsAliasFor(Binary):
    def __init__(self):
        Binary.__init__(self)
        
        self.name = self.__class__.__name__
        
        for (k, v) in __classmapf__.items():
            if v == self.__class__:
                self.desc = k
        for (k, v) in __classmapb__.items():
            if v == self.__class__:
                self.backwardsDesc = k

@caseclass.caseclass
@types.argtypes()
class IsAlignedWith(Binary):
    def __init__(self):
        Binary.__init__(self)
        
        self.name = self.__class__.__name__
        
        for (k, v) in __classmapf__.items():
            if v == self.__class__:
                self.desc = k
        for (k, v) in __classmapb__.items():
            if v == self.__class__:
                self.backwardsDesc = k
__classmapf__ = {
    "depends on": DependsOn, 
    "has meta-theory": HasMeta, 
    "includes": Includes, 
    "has domain": HasDomain, 
    "has codomain": HasCodomain, 
    "is instance of": IsInstanceOf, 
    "refers to": RefersTo, 
    "contains declaration of": Declares, 
    "is alias for": IsAliasFor, 
    "is aligned with": IsAlignedWith
}

__classmapb__ = {
    "depended on by": DependsOn, 
    "is meta-theory of": HasMeta, 
    "included by": Includes, 
    "is domain of": HasDomain, 
    "is codomain of": HasCodomain, 
    "instantiates": IsInstanceOf, 
    "is refered to by": RefersTo, 
    "is declared in": Declares, 
    "has alias": IsAliasFor, 
    "is aligned with": IsAlignedWith
}
