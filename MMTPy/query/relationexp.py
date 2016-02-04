"""
    RelationExp = 
        ToObject( dep : Binary)
        ToSubject (dep : Binary)
        Transitive ( q : RelationExp)
        Choice(qs : List[RelationExp])
        Sequence(qs : List[RelationExp])
        Reflexive()
        HasType(tp : Unary)
        
        symmetric === Choice([q, -q])
"""

from MMTPy import xml

class RelationExp(object):
    def __init__(self):
        pass
    @staticmethod
    def fromXML(node):
        if xml.matches(node, "sequence"):
            from MMTPy.query.relationexps import Sequence
            return Sequence.fromXML(node)
            
        if xml.matches(node, "choice"):
            from MMTPy.query.relationexps import Choice
            return Choice.fromXML(node)
        
        if xml.matches(node, "transitive"):
            from MMTPy.query.relationexps import Transitive
            return Transitive.fromXML(node)
        
        if xml.matches(node, "reflexive"):
            from MMTPy.query.relationexps import Reflexive
            return Reflexive.fromXML(node)
        
        if xml.matches(node, "inverse"):
            return -RelationExp.fromXML(node[0])
        
        if xml.matches(node, "toobject"):
            from MMTPy.query.relationexps import ToObject
            return ToObject.fromXML(node)
        
        if xml.matches(node, "tosubject"):
            from MMTPy.query.relationexps import ToSubject
            return ToSubject.fromXML(node)
        
        if xml.matches(node, "hastype"):
            from MMTPy.query.relationexps import HasType
            return HasType.fromXML(node)
        
        raise ValueError("invalid RelationExp")