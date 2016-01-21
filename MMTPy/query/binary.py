from MMTPy.caseclass import caseclass, types
# TODO: Figure out custom binary

class Binary(object):
    @staticmethod
    def parse(s):
        for (k, v) in __classmapf__.items():
            if v.__name__ == s:
                return v()
        raise ValueError("Unknown Binary")

class DependsOn(caseclass.make(), Binary):
    def __init__(self):
        super(DependsOn, self).__init__()
        self.name = self.__class__.__name__
        
        for (k, v) in __classmapf__.items():
            if v == self.__class__:
                self.desc = k
        for (k, v) in __classmapb__.items():
            if v == self.__class__:
                self.backwardsDesc = k
class HasMeta(caseclass.make(), Binary):
    def __init__(self):
        super(HasMeta, self).__init__()
        self.name = self.__class__.__name__
        
        for (k, v) in __classmapf__.items():
            if v == self.__class__:
                self.desc = k
        for (k, v) in __classmapb__.items():
            if v == self.__class__:
                self.backwardsDesc = k
class Includes(caseclass.make(), Binary):
    def __init__(self):
        super(Includes, self).__init__()
        self.name = self.__class__.__name__
        
        for (k, v) in __classmapf__.items():
            if v == self.__class__:
                self.desc = k
        for (k, v) in __classmapb__.items():
            if v == self.__class__:
                self.backwardsDesc = k
class HasDomain(caseclass.make(), Binary):
    def __init__(self):
        super(HasDomain, self).__init__()
        self.name = self.__class__.__name__
        
        for (k, v) in __classmapf__.items():
            if v == self.__class__:
                self.desc = k
        for (k, v) in __classmapb__.items():
            if v == self.__class__:
                self.backwardsDesc = k
class HasCodomain(caseclass.make(), Binary):
    def __init__(self):
        super(HasCodomain, self).__init__()
        self.name = self.__class__.__name__
        
        for (k, v) in __classmapf__.items():
            if v == self.__class__:
                self.desc = k
        for (k, v) in __classmapb__.items():
            if v == self.__class__:
                self.backwardsDesc = k
class IsInstanceOf(caseclass.make(), Binary):
    def __init__(self):
        super(IsInstanceOf, self).__init__()
        self.name = self.__class__.__name__
        
        for (k, v) in __classmapf__.items():
            if v == self.__class__:
                self.desc = k
        for (k, v) in __classmapb__.items():
            if v == self.__class__:
                self.backwardsDesc = k
class RefersTo(caseclass.make(), Binary):
    def __init__(self):
        super(RefersTo, self).__init__()
        self.name = self.__class__.__name__
        
        for (k, v) in __classmapf__.items():
            if v == self.__class__:
                self.desc = k
        for (k, v) in __classmapb__.items():
            if v == self.__class__:
                self.backwardsDesc = k
class Declares(caseclass.make(), Binary):
    def __init__(self):
        super(Declares, self).__init__()
        self.name = self.__class__.__name__
        
        for (k, v) in __classmapf__.items():
            if v == self.__class__:
                self.desc = k
        for (k, v) in __classmapb__.items():
            if v == self.__class__:
                self.backwardsDesc = k
class IsAliasFor(caseclass.make(), Binary):
    def __init__(self):
        super(IsAliasFor, self).__init__()
        self.name = self.__class__.__name__
        
        for (k, v) in __classmapf__.items():
            if v == self.__class__:
                self.desc = k
        for (k, v) in __classmapb__.items():
            if v == self.__class__:
                self.backwardsDesc = k
class IsAlignedWith(caseclass.make(), Binary):
    def __init__(self):
        super(IsAlignedWith, self).__init__()
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
