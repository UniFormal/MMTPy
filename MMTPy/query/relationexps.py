from MMTPy import xml
from MMTPy.clsutils import caseclass, types


from MMTPy.query.relationexp import RelationExp
from MMTPy.query.unary import Unary
from MMTPy.query.binary import Binary

@caseclass.caseclass
@types.argtypes(Binary)
class ToObject(RelationExp):
    def __init__(self, dep):
        super(ToObject, self).__init__()

        self.dep = dep
    def __neg__(self):
        return ToSubject(self.dep)
    def toXML(self):
        return xml.make_element("toobject", relation=self.dep.name)
    @staticmethod
    def fromXML(self):
        if xml.matches(node, "toobject"):
            return ToObject(Binary.parse(node.attrib.get("relation")))
        else:
            raise ValueError("INVALID <TOOBJECT/>")

@caseclass.caseclass
@types.argtypes(Binary)
class ToSubject(RelationExp):
    def __init__(self, dep):
        super(ToSubject, self).__init__()

        self.dep = dep
    def __neg__(self):
        return ToObject(self.dep)
    def toXML(self):
        return xml.make_element("tosubject", relation=self.dep.name)
    @staticmethod
    def fromXML(self):
        if xml.matches(node, "tosubject"):
            return ToSubject(Binary.parse(node.attrib.get("relation")))
        else:
            raise ValueError("INVALID <TOOBJECT/>")

@caseclass.caseclass
@types.argtypes(RelationExp)
class Transitive(RelationExp):
    def __init__(self, q):
        super(Transitive, self).__init__()

        self.q = q
    def __neg__(self):
        return Transitive(-self.q)
    def toXML(self):
        return xml.make_element("transitive", self.q.toXML())
    @staticmethod
    def fromXML(self):
        if xml.matches(node, ("transitive", (None, ))):
            return Transitive(RelationExp.fromXML(node[0]))
        else:
            raise ValueError("INVALID <transitive/>")

@caseclass.caseclass
@types.argtypes([RelationExp])
class Choice(RelationExp):
    def __init__(self, qs):
        super(Choice, self).__init__()

        self.qs = qs
    def __neg__(self):
        return Choice(list(map(lambda s:-s, self.qs)))
    def toXML(self):
        return xml.make_element("choice", *map(lambda q:q.toXML(), self.qs))
    @staticmethod
    def fromXML(self):
        if xml.matches(node, "choice"):
            return Choice([RelationExp.fromXML(c) for c in node])
        else:
            raise ValueError("INVALID <choice/>")

@caseclass.caseclass
@types.argtypes([RelationExp])
class Sequence(RelationExp):
    def __init__(self, qs):
        super(Sequence, self).__init__()

        self.qs = qs
    def __neg__(self):
        return Sequence(list(map(lambda s:-s, self.qs)))
    def toXML(self):
        return xml.make_element("sequence", *map(lambda q:q.toXML(), self.qs))
    @staticmethod
    def fromXML(self):
        if xml.matches(node, "sequence"):
            return Sequence([RelationExp.fromXML(c) for c in node])
        else:
            raise ValueError("INVALID <sequence/>")

@caseclass.caseclass
@types.argtypes()
class Reflexive(RelationExp):
    def __neg__(self):
        return self
    def toXML(self):
        return xml.make_element("reflexive")
    @staticmethod
    def fromXML(self):
        if xml.matches(node, "reflexive"):
            return Reflexive()
        else:
            raise ValueError("INVALID <reflexive/>")

@caseclass.caseclass
@types.argtypes(Unary)
class HasType(RelationExp):
    def __init__(self, tp):
        super(HasType, self).__init__()

        self.tp = tp
    def __neg__(self):
        return self
    def toXML(self):
        return xml.make_element("hastype", concept=self.tp.s)
    @staticmethod
    def fromXML(self):
        if xml.matches(node, "hastype"):
            return HasType(Unary.parse(node.attrib.get("concept")))
        else:
            raise ValueError("INVALID <reflexive/>")

def Symmetric(q):
    return Choice(q, -q)
