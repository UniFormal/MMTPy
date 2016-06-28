from MMTPy import xml

from MMTPy.clsutils import caseclass, types
from MMTPy.content import componentkey

from MMTPy.query.query import Query
from MMTPy.query.prop import Prop
from MMTPy.query.unary import Unary
from MMTPy.query.relationexp import RelationExp

from MMTPy.paths import path
from MMTPy.content.objects import obj
from MMTPy.content import position
from MMTPy.dependencies import etree_type

@caseclass.caseclass
@types.argtypes(Query, Query)
class BigUnion(Query):
    def __init__(self, domain, of):
        super(BigUnion, self).__init__()

        self.domain = domain
        self.of = of
    def toXML(self):
        # TODO: Figure out the type argument
        return xml.make_element("bigunion", self.domain.toXML(), self.of.toXML(), type="path")
    @staticmethod
    def fromXML(node):
        if xml.matches(node, ("bigunion", (None, None))):
            return BigUnion(Query.fromXML(node[0]), Query.fromXML(node[1]))
        else:
            raise ValueError("not a valid <BIGUNION/>")

@caseclass.caseclass
@types.argtypes(int)
class Bound(Query):
    def __init__(self, index):
        super(Bound, self).__init__()

        self.index = index
    def toXML(self):
        return xml.make_element("bound", index=self.idx)
    @staticmethod
    def fromXML(node):
        if xml.matches(node, "bound"):
            return Bound(int(node.attrib.get("index")))
        else:
            raise ValueError("not a valid <BOUND/>")

@caseclass.caseclass
@types.argtypes(Query)
class Closure(Query):
    def __init__(self, of):
        super(Closure, self).__init__()

        self.of = of
    def toXML(self):
        return xml.make_element("closure", self.of.toXML())
    @staticmethod
    def fromXML(node):
        if xml.matches(node, ("closure", (None,))):
            return Closure(Query.fromXML(node[0]))
        else:
            raise ValueError("not a valid <CLOSURE/>")

@caseclass.caseclass
@types.argtypes(Query, componentkey.ComponentKey)
class Component(Query):
    def __init__(self, of, component):
        super(Component, self).__init__()

        self.of = of
        self.component = component
    def toXML(self):
        return xml.make_element("component", self.of.toXML(), index=self.component.s)
    @staticmethod
    def fromXML(node):
        if xml.matches(node, ("closure", (None,))):
            return Component(Query.fromXML(node[0]), componentkey.ComponentKey.parse(node.attr("index")))
        else:
            raise ValueError("not a valid <COMPONENT/>")

@caseclass.caseclass
@types.argtypes(Query, Prop)
class Comprehension(Query):
    def __init__(self, domain, pred):
        super(Comprehension, self).__init__()

        self.domain = domain
        self.pred = pred
    def toXML(self):
        return xml.make_element("comprehension", self.domain.toXML(), self.pred.toXML())
    @staticmethod
    def fromXML(node):
        if xml.matches(node, ("comprehension", (None, None))):
            return Comprehension(Query.fromXML(node[0]), Prop.fromXML(node[1]))
        else:
            raise ValueError("not a valid <comprehension/>")

@caseclass.caseclass
@types.argtypes(Query, Query)
class Let(Query):
    def __init__(self, value, i):
        super(Let, self).__init__()

        self.value = value
        self.i = i
    def toXML(self):
        return xml.make_element("let", self.value.toXML(), self.i.toXML())
    @staticmethod
    def fromXML(node):
        if xml.matches(node, ("let", (None, None))):
            return Let(Query.fromXML(node[0]), Query.fromXML(node[1]))
        else:
            raise ValueError("not a valid <LET/>")

@caseclass.caseclass
@types.argtypes(object)
class Literal(Query):
    def __init__(self, literal):
        super(Literal, self).__init__()

        self.literal = literal
    def toXML(self):
        if isinstance(self.literal, path.Path):
            lox = xml.make_element("uri", path=self.literal)
        elif isinstance(self.literal, types.strtype):
            lox = xml.make_element("string")
            lox.text = self.literal
        elif isinstance(self.literal, obj.Obj):
            lox = xml.make_element("object", self.literal.toOBJXML())
        elif isinstance(self.literal, etree_type):
            lox = xml.make_element("xml", xml.copy(self.literal))
        else:
            raise ValueError("unknown literal type %s" % type(self.literal))

        return xml.make_element("literal", lox)
    @staticmethod
    def fromXML(node):
        if xml.matches(node, "literal"):
            if "uri" in node.attrib:
                # backward compatibility
                return Literal(path.Path.parse(node.attrib.get("uri")))
            elif len(node) > 0:
                lox = node[0]

                if xml.matches(lox, "uri"):
                    return Literal(path.Path.parse(lox.attrib.get("path")))
                elif xml.matches(lox, "string"):
                    return Literal(lox.text)
                elif xml.matches(lox, "object"):
                    return Literal(obj.Obj.fromXML(lox[0]))
                elif xml.matches(lox, "xml"):
                    return Literal(lox[0])
                else:
                    raise ValueError("unknown literal type")
            else:
                # backward compatibility
                return Literal(node.text)
        else:
            raise ValueError("not a valid <literal/>")

@caseclass.caseclass
@types.argtypes(Unary)
class Paths(Query):
    def __init__(self, tp):
        super(Paths, self).__init__()

        self.tp = tp
    def toXML(self):
        return xml.make_element("uris", concept=self.tp.s)
    @staticmethod
    def fromXML(node):
        if xml.matches(node, "uris"):
            return Paths(Unary.parse(node.attrib.get("concept")))
        else:
            raise ValueError("not a valid <PATHS/>")

@caseclass.caseclass
@types.argtypes(Query, int)
class Projection(Query):
    def __init__(self, of, index):
        super(Projection, self).__init__()

        self.of = of
        self.index = index
    def toXML(self):
        return xml.make_element("projection", self.of.toXML(), index=self.idx)
    @staticmethod
    def fromXML(node):
        if xml.matches(node, ("projection", (None, ))):
            return Projection(Query.fromXML(node[0]), int(node.attrib.get("index")))
        else:
            raise ValueError("not a valid <projection/>")

@caseclass.caseclass
@types.argtypes(types.strtype, Query, [types.strtype])
class QueryFunctionApply(Query):
    def __init__(self, function, argument, params):
        super(QueryFunctionApply, self).__init__()

        self.function = function
        self.argument = argument
        self.params = params
    def toXML(self):
        return xml.make_element("function", self.argument.toXML(), name=self.function, param=",".join(self.params))
    @staticmethod
    def fromXML(node):
        if xml.matches(node, ("function", (None, ))):
            return QueryFunctionApply(node.attrib.get("name"), Query.fromXML(node[0]), node.attrib.get("param").split(","))
        else:
            raise ValueError("not a valid <projection/>")


@caseclass.caseclass
@types.argtypes(Query, RelationExp)
class Related(Query):
    def __init__(self, to, by):
        super(Related, self).__init__()

        self.to = to
        self.by = by
    def toXML(self):
        return xml.make_element("related", self.to.toXML(), self.by.toXML())
    @staticmethod
    def fromXML(node):
        if xml.matches(node, ("related", (None, None))):
            return Related(Query.fromXML(node[0]), RelationExp.fromXML(node[1]))
        else:
            raise ValueError("not a valid <related/>")

@caseclass.caseclass
@types.argtypes(Query)
class Singleton(Query):
    def __init__(self, e):
        super(Singleton, self).__init__()

        self.e = e
    def toXML(self):
        return xml.make_element("singleton", self.e.toXML())
    @staticmethod
    def fromXML(node):
        if xml.matches(node, ("singleton", (None,))):
            return Singleton(Query.fromXML(node[0]))
        else:
            raise ValueError("not a valid <singleton/>")

@caseclass.caseclass
@types.argtypes(Query, position.Position)
class SubObject(Query):
    def __init__(self, of, position):
        super(SubObject, self).__init__()

        self.of = of
        self.position = position
    def toXML(self):
        return xml.make_element("subobject", self.of.toXML(), position=str(self.position))
    @staticmethod
    def fromXML(node):
        if xml.matches(node, ("subobject", (None,))):
            return SubObject(Query.fromXML(node[0]), position.Position.parse(node.attrib.get("position")))
        else:
            raise ValueError("not a valid <subobject/>")

@caseclass.caseclass
@types.argtypes([Query])
class Tuple(Query):
    def __init__(self, components):
        super(Tuple, self).__init__()

        self.components = components
    def toXML(self):
        return xml.make_element("tuple", *map(lambda c:c.toXML(), self.components))
    @staticmethod
    def fromXML(node):
        if xml.matches(node, "tuple"):
            return Tuple([Query.fromXML(c) for c in node])
        else:
            raise ValueError("not a valid <tuple/>")

@caseclass.caseclass
@types.argtypes(obj.Obj)
class Unifies(Query):
    def __init__(self, wth):
        super(Unifies, self).__init__()

        self.wth = wth
    def toXML(self):
        return xml.make_element("unifies", self.wth.toXML())
    @staticmethod
    def fromXML(node):
        if xml.matches(node, ("unifies", (None,))):
            return Unifies(obj.Obj.fromXML(node[0]))
        else:
            raise ValueError("not a valid <unifies/>")

@caseclass.caseclass
@types.argtypes(Query, Query)
class Union(Query):
    def __init__(self, left, right):
        super(Union, self).__init__()

        self.left = left
        self.right = right
    def toXML(self):
        return xml.make_element("union", self.left.toXML(), self.right.toXML())
    @staticmethod
    def fromXML(node):
        if xml.matches(node, ("union", (None, None))):
            return Union(Query.fromXML(node[0]), Query.fromXML(node[1]))
        else:
            raise ValueError("not a valid <UNION/>")
