"""
Query = 
    BigUnion(domain: Query, of: Query)
    Bound(index: Int)
    Closure(of: Query)
    Component(of: Query, component: ComponentKey)
    Comprehension(domain: Query, pred: Prop)
    Let(value: Query, in: Query)
    Literal[T <: BaseType](literal: T)
    // UNIMPLEMENTED Literals[T <: BaseType](literals: T*)
    Paths(tp: Unary)
    Projection(of: Query, index: Int)
    // TODO: QueryFunctionApply(function: String, argument: Query, params: List[String])
    Related(to: Query, by: RelationExp)
    Singleton(e: Query)
    SubObject(of: Query, position: Position)
    Tuple(components: List[Query])
    Unifies(wth: Obj)
    Union(left: Query, right: Query)
"""
from MMTPy import xml

class Query(object):
    @staticmethod
    def parse(node):
        if xml.matches(node, "bigunion"):
            from MMTPy.query.queries import BigUnion
            return BigUnion.fromXML(node)
        
        if xml.matches(node, "bound"):
            from MMTPy.query.queries import Bound
            return bound.Bound.fromXML(node)
        
        if xml.matches(node, "closure"):
            from MMTPy.query.queries import Closure
            return Closure.fromXML(node)
        
        if xml.matches(node, "component"):
            from MMTPy.query.queries import Component
            return Component.fromXML(node)
        
        if xml.matches(node, "comprehension"):
            from MMTPy.query.queries import Comprehension
            return Comprehension.fromXML(node)
        
        if xml.matches(node, "let"):
            from MMTPy.query.queries import Let
            return Let.fromXML(node)
        
        if xml.matches(node, "literal"):
            from MMTPy.query.queries import Literal
            return Literal.fromXML(node)
        
        if xml.matches(node, "paths"):
            from MMTPy.query.queries import Paths
            return Paths.fromXML(node)
            
        if xml.matches(node, "projection"):
            from MMTPy.query.queries import Projection
            return Projection.fromXML(node)
        
        if xml.matches(node, "function"):
            from MMTPy.query.queries import QueryFunctionApply
            return QueryFunctionApply.fromXML(node)
        
        if xml.matches(node, "related"):
            from MMTPy.query.queries import Related
            return Related.fromXML(node)
        
        if xml.matches(node, "singleton"):
            from MMTPy.query.queries import Singleton
            return Singleton.fromXML(node)
        
        if xml.matches(node, "subobject"):
            from MMTPy.query.queries import SubObject
            return SubObject.fromXML(node)
        
        if xml.matches(node, "tuple"):
            from MMTPy.query.queries import Tuple
            return Tuple.fromXML(node)
        
        if xml.matches(node, "unifies"):
            from MMTPy.query.queries import Unifies
            return Unifies.fromXML(node)
        
        if xml.matches(node, "union"):
            from MMTPy.query.queries import Union
            return Union.fromXML(node)
        
        raise ValueError("not a valid Query object")