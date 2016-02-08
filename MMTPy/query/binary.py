from MMTPy.clsutils import caseclass, types
# TODO: Figure out custom binary

class Binary(object):
    def __init__(self, name, desc, backwardsDesc):
        self.name = name
        self.desc = desc
        self.backwardsDesc = backwardsDesc

    @staticmethod
    def parse(s):
        for (k, v) in __classmap__.items():
            if v.__name__ == s:
                return v()
        raise ValueError("Unknown Binary")

@caseclass.caseclass
@types.argtypes()
class DependsOn(Binary):
    def __init__(self):
        super(DependsOn, self).__init__("DependsOn", "depends on", "depended on by")

@caseclass.caseclass
@types.argtypes()
class HasMeta(Binary):
    def __init__(self):
        super(HasMeta, self).__init__("HasMeta", "has meta-theory", "is meta-theory of")

@caseclass.caseclass
@types.argtypes()
class Includes(Binary):
    def __init__(self):
        super(Includes, self).__init__("Includes", "includes", "included by")

@caseclass.caseclass
@types.argtypes()
class HasDomain(Binary):
    def __init__(self):
        super(HasDomain, self).__init__("HasDomain", "has domain", "is domain of")

@caseclass.caseclass
@types.argtypes()
class HasCodomain(Binary):
    def __init__(self):
        super(HasCodomain, self).__init__("HasDomain", "has codomain", "is codomain of")

@caseclass.caseclass
@types.argtypes()
class IsInstanceOf(Binary):
    def __init__(self):
        super(IsInstanceOf, self).__init__("IsInstanceOf", "is instance of", "instantiates")

@caseclass.caseclass
@types.argtypes()
class RefersTo(Binary):
    def __init__(self):
        super(RefersTo, self).__init__("RefersTo", "refers to", "is refered to by")

@caseclass.caseclass
@types.argtypes()
class Declares(Binary):
    def __init__(self):
        super(Declares, self).__init__("Declares", "contains declaration of", "is declared in")

@caseclass.caseclass
@types.argtypes()
class IsAliasFor(Binary):
    def __init__(self):
        super(IsAliasFor, self).__init__("IsAliasFor", "is alias for", "has alias")

@caseclass.caseclass
@types.argtypes()
class IsAlignedWith(Binary):
    def __init__(self):
        super(IsAlignedWith, self).__init__("IsAliasFor", "is aligned with", "is aligned with")

__classmap__ = {
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
