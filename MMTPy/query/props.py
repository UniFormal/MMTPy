from MMTPy import xml
from MMTPy.caseclass import caseclass

from MMTPy.query.prop import Prop
from MMTPy.query.query import Query
from MMTPy.query.unary import Unary

class And(caseclass.make(Prop, Prop), Prop):
    def __init__(self, left, right):
        super(And, self).__init__(left, right)
        self.left = left
        self.right = right
    def toXML(self):
        return xml.make_element("and", self.left.toXML(), self.right.toXML())
    @staticmethod
    def fromXML(node):
        if xml.matches(node, ("and", (None, None))):
            return And(Prop.fromXML(node[0]), Prop.fromXML(node[1]))

class Equal(caseclass.make(Query, Query), Prop):
    def __init__(self, left, right):
        super(Equal, self).__init__(left, right)
        self.left = left
        self.right = right
    def toXML(self):
        return xml.make_element("equal", self.left.toXML(), self.right.toXML())
    @staticmethod
    def fromXML(node):
        if xml.matches(node, ("equal", (None, None))):
            return Equal(Query.fromXML(node[0]), Query.fromXML(node[1]))

class Forall(caseclass.make(Query, Prop), Prop):
    def __init__(self, domain, scope):
        super(Forall, self).__init__(domain, scope)
        self.domain = domain
        self.scope = scope
    def toXML(self):
        return xml.make_element("forall", self.domain.toXML(), self.scope.toXML())
    @staticmethod
    def fromXML(node):
        if xml.matches(node, ("forall", (None, None))):
            return Forall(Query.fromXML(node[0]), Prop.fromXML(node[1]))

class IsA(caseclass.make(Query, Unary), Prop):
    def __init__(self, e, t):
        super(IsA, self).__init__(e, t)
        self.e = e
        self.t = t
    def toXML(self):
        return xml.make_element("isa", self.e.toXML(), concept=self.t.s)
    @staticmethod
    def fromXML(node):
        if xml.matches(node, ("isa", (None,))):
            return IsA(Query.fromXML(node[0]), Unary.parse(node.attrib.get("concept")))

class IsEmpty(caseclass.make(Query), Prop):
    def __init__(self, r):
        super(Forall, self).__init__(r)
        self.r = r
    def toXML(self):
        return xml.make_element("isempty", self.r.toXML())
    @staticmethod
    def fromXML(node):
        if xml.matches(node, ("isempty", (None,))):
            return Equal(Query.fromXML(node[0]))

class IsIn(caseclass.make(Query, Query), Prop):
    def __init__(self, elem, tp):
        super(IsIn, self).__init__(elem, tp)
        self.elem = elem
        self.tp = tp
    def toXML(self):
        return xml.make_element("isin", self.elem.toXML(), self.tp.toXML())
    @staticmethod
    def fromXML(node):
        if xml.matches(node, ("isin", (None, None))):
            return IsIn(Query.fromXML(node[0]), Query.fromXML(node[1]))

class Not(caseclass.make(Prop), Prop):
    def __init__(self, arg):
        super(Not, self).__init__(arg)
        self.arg = arg
    def toXML(self):
        return xml.make_element("not", self.arg.toXML())
    @staticmethod
    def fromXML(node):
        if xml.matches(node, ("not", (None,))):
            return Not(Prop.fromXML(node[0]))

class PrefixOf(caseclass.make(Query, Query), Prop):
    def __init__(self, short, lg):
        super(PrefixOf, self).__init__(short, lg)
        self.short = short
        self.long = lg
    def toXML(self):
        return xml.make_element("prefixof", self.short.toXML(), self.long.toXML())
    @staticmethod
    def fromXML(node):
        if xml.matches(node, ("prefixof", (None, None))):
            return PrefixOf(Query.fromXML(node[0]), Query.fromXML(node[1]))