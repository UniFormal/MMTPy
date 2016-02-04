from MMTPy import xml

"""
Prop = 
    And(left: prop, right: prop)
    Equal(left : query, right : query)
    Forall(domain : query, scope : prop)
    IsA(e : query, t : Unary)
    IsEmpty(r : query)
    IsIn(elem : query, tp: query)
    Not(arg : prop)
    PrefixOf(short : query, long: query)
"""

class Prop(object):
    def __init__(self):
        pass
    
    @staticmethod
    def fromXML(node):
        if xml.matches(node, "and"):
            from MMTPy.query.props import And
            return And.fromXML(node)
        
        if xml.matches(node, "equal"):
            from MMTPy.query.props import Equal
            return Equal.fromXML(node)
        
        if xml.matches(node, "forall"):
            from MMTPy.query.props import Forall
            return Forall.fromXML(node)
        
        if xml.matches(node, "isa"):
            from MMTPy.query.props import IsA
            return IsA.fromXML(node)
        
        if xml.matches(node, "isempty"):
            from MMTPy.query.props import IsEmpty
            return IsEmpty.fromXML(node)
        
        if xml.matches(node, "isin"):
            from MMTPy.query.props import IsIn
            return IsIn.fromXML(node)
        
        if xml.matches(node, "not"):
            from MMTPy.query.props import Not
            return Not.fromXML(node)
        
        if xml.matches(node, "prefixof"):
            from MMTPy.query.props import PrefixOf
            return PrefixOf.fromXML(node)
        
        raise ValueError("invalid prop")