from MMTPy import xml
from MMTPy.clsutils import caseclass, types

from MMTPy.query.prop import Prop
from MMTPy.query.query import Query
from MMTPy.query.unary import Unary

@caseclass.caseclass
@types.argtypes(Prop, Prop)
class And(Prop):
    def __init__(self, left, right):
        Prop.__init__(self)
        
        self.left = left
        self.right = right
    def toXML(self):
        return xml.make_element("and", self.left.toXML(), self.right.toXML())
    @staticmethod
    def fromXML(node):
        if xml.matches(node, ("and", (None, None))):
            return And(Prop.fromXML(node[0]), Prop.fromXML(node[1]))

@caseclass.caseclass
@types.argtypes(Query, Query)
class Equal(Prop):
    def __init__(self, left, right):
        Prop.__init__(self)
        
        self.left = left
        self.right = right
    def toXML(self):
        return xml.make_element("equal", self.left.toXML(), self.right.toXML())
    @staticmethod
    def fromXML(node):
        if xml.matches(node, ("equal", (None, None))):
            return Equal(Query.fromXML(node[0]), Query.fromXML(node[1]))

@caseclass.caseclass
@types.argtypes(Query, Prop)
class Forall(Prop):
    def __init__(self, domain, scope):
        Prop.__init__(self)
        
        self.domain = domain
        self.scope = scope
    def toXML(self):
        return xml.make_element("forall", self.domain.toXML(), self.scope.toXML())
    @staticmethod
    def fromXML(node):
        if xml.matches(node, ("forall", (None, None))):
            return Forall(Query.fromXML(node[0]), Prop.fromXML(node[1]))

@caseclass.caseclass
@types.argtypes(Query, Unary)
class IsA(Prop):
    def __init__(self, e, t):
        Prop.__init__(self)
        
        self.e = e
        self.t = t
    def toXML(self):
        return xml.make_element("isa", self.e.toXML(), concept=self.t.s)
    @staticmethod
    def fromXML(node):
        if xml.matches(node, ("isa", (None,))):
            return IsA(Query.fromXML(node[0]), Unary.parse(node.attrib.get("concept")))

@caseclass.caseclass
@types.argtypes(Query)
class IsEmpty(Prop):
    def __init__(self, r):
        Prop.__init__(self)
        
        self.r = r
    def toXML(self):
        return xml.make_element("isempty", self.r.toXML())
    @staticmethod
    def fromXML(node):
        if xml.matches(node, ("isempty", (None,))):
            return Equal(Query.fromXML(node[0]))

@caseclass.caseclass
@types.argtypes(Query, Query)
class IsIn(Prop):
    def __init__(self, elem, tp):
        Prop.__init__(self)
        
        self.elem = elem
        self.tp = tp
    def toXML(self):
        return xml.make_element("isin", self.elem.toXML(), self.tp.toXML())
    @staticmethod
    def fromXML(node):
        if xml.matches(node, ("isin", (None, None))):
            return IsIn(Query.fromXML(node[0]), Query.fromXML(node[1]))

@caseclass.caseclass
@types.argtypes(Prop)
class Not(Prop):
    def __init__(self, arg):
        Prop.__init__(self)
        
        self.arg = arg
    def toXML(self):
        return xml.make_element("not", self.arg.toXML())
    @staticmethod
    def fromXML(node):
        if xml.matches(node, ("not", (None,))):
            return Not(Prop.fromXML(node[0]))

@caseclass.caseclass
@types.argtypes(Query, Query)
class PrefixOf(Prop):
    def __init__(self, short, lg):
        Prop.__init__(self)
        
        self.short = short
        self.long = lg
    def toXML(self):
        return xml.make_element("prefixof", self.short.toXML(), self.long.toXML())
    @staticmethod
    def fromXML(node):
        if xml.matches(node, ("prefixof", (None, None))):
            return PrefixOf(Query.fromXML(node[0]), Query.fromXML(node[1]))