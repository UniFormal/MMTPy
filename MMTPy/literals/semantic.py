from MMTPy.caseclass import types
class SemanticType(object):
    """
    A SemanticType represents a native python type that can be used with literals
    """
    def __init__(self):
        pass
    def fromString(self, obj):
        """
        Takes a string representation of this type and returns a coresponding
        native python object.
        """
        pass
    def toString(self, obj):
        """
        Takes a native Python object and turns it into a string representation
        using this semantic type.
        """
        pass
    def normalform(self, obj):
        """
        Turns an object into a normal form. Defaults to the identity.
        """
        return obj
    def valid(self, obj):
        """
        Checks if this SemanticType is Applicable to a given python object.
        """
        return True
    def isApplicable(self, obj):
        """
        Checks if this SemanticType is Applicable to a given object
        """
        return True

class ListType(SemanticType):
    def __init__(self, tp):
        super(ListType, self).__init__()
        self.tp = tp
        self.name = "List["+tp.name+"]"
    def fromString(self, obj):
        if (not obj.startswith("[")) or (not obj.endswith("]")):
            raise ValueError("expected value to be a list")
        return list(map(lambda x:self.tp.fromString(x), ",".split(obj[1:-1])))
    def normalform(self, obj):
        return list(map(self.normalform, obj))
    def valid(self, obj):
        if isinstance(obj, list):
            for o in obj:
                if not self.tp.valid(o):
                    return False
            return True
        else:
            return False
        if isinstance(obj, tuple):
            if len(obj) == 2:
                (l, r) = obj
                return self.left.valid(l) and self.right.valid(r)

        return False
    def toString(self, obj):
        return "[%s]" % (",".join(map(lambda x:self.tp.toString(x), obj)))

class ProductType(SemanticType):
    def __init__(self, left, right):
        super(ProductType, self).__init__()
        self.left = left
        self.right = right
        self.name = "Product["+left.name+","+right.name+"]"
    def normalform(self, obj):
        (l, r) = obj
        return (
            self.left.normalform(l),
            self.right.normalform(r)
        )
    def valid(self, obj):
        if isinstance(obj, tuple):
            if len(obj) == 2:
                (l, r) = obj
                return self.left.valid(l) and self.right.valid(r)

        return False
    def fromString(self, obj):
        if (not obj.startswith("(")) or (not obj.endswith(")")):
            raise ValueError("expected value to be a pair")

        splt = ",".split(obj[1:-1])
        if len(splt) != 2:
            raise ValueError("expected value to be a pair")

        return (self.left.fromString(splt[0]), self.right.fromString(splt[1]))

class TupleType(ListType):
    def __init__(self, tp, dim):
        super(TupleType, self).__init__(tp)
        self.dim = dim
        self.name = "Tuple["+tp.name+"]"
    def fromString(self, obj):
        if (not obj.startswith("(")) or (not obj.endswith(")")):
            raise ValueError("expected value to be a list")
        return list(map(lambda x:self.tp.fromString(x), ",".split(obj[1:-1])))
    def normalform(self, obj):
        return tuple(super(TupleType, self).normalform(obj))
    def valid(self, obj):
        return super(TupleType, self).valid(obj) and len(obj) == self.dim
    def toString(self, obj):
        return "(%s)" % (",".join(map(lambda x:self.tp.toString(x), obj)))

class SubType(SemanticType):
    def __init__(self, of):
        super(SemanticType, self).__init__()
        self.of = of
        self.name = "SubType["+of.name+"]"
    def by(self, obj):
        raise NotImplementedError
    def fromString(self, obj):
        return self.of.fromString(obj)
    def normalform(self, obj):
        return self.of.normalform(obj)
    def valid(self, obj):
        return self.of.valid(obj) and self.by(obj)
    def toString(self, obj):
        return self.of.toString(obj)

class Quotient(SemanticType):
    def __init__(self, of):
        super(Quotient, self).__init__()
        self.of = of
        self.name = "Quotient["+of.name+"]"
    def by(self, obj):
        raise NotImplementedError
    def fromString(self, obj):
        return self.by(self.of.fromString(obj))
    def normalform(self, obj):
        return self.by(self.of.normalform(obj))
    def valid(self, obj):
        return self.of.valid(obj) and self.by(obj)
    def toString(self, obj):
        return self.of.toString(self.by(obj))

class RepresentationType(SemanticType):
    def __init__(self, c):
        super(RepresentationType, self).__init__()
        self.cls = c
        self.name = "RepresentationType["+c.__name__+"]"
    def valid(self, obj):
        return isinstance(obj, self.cls)
    def toString(self, obj):
        return str(obj)
    def fromString(self, obj):
        return self.cls(obj)

class StandardInt(RepresentationType):
    def __init__(self):
        super(StandardInt, self).__init__(int)
        self.name = "Int"

class StandardNat(SubType):
    def __init__(self):
        super(StandardNat, self).__init__(StandardInt())
        self.name = "Nat"
    def by(self, obj):
        return obj >= 0

class StandardString(RepresentationType):
    def __init__(self):
        super(StandardString, self).__init__(types.strtype)
        self.name = "String"
    def fromString(self, obj):
        return obj
    def toString(self, obj):
        return obj

class StandardBool(RepresentationType):
    def __init__(self):
        super(StandardBool, self).__init__(bool)
        self.name = "Bool"
    def fromString(self, obj):
        return obj == "true"
    def toString(self, obj):
        return "true" if obj else "false"

class StandardDouble(RepresentationType):
    def __init__(self):
        super(StandardDouble, self).__init__(float)
        self.name = "Double"

from MMTPy.objects import URI
class URILiteral(RepresentationType):
    def __init__(self):
        super(URILiteral, self).__init__(URI.URI)
        self.name = "URI"
    def fromString(self, obj):
        return URI.URI.fromString(obj)
