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
    def isApplicable(self, obj):
        """
        Checks if this SemanticType is Applicable to a given object
        """
        return True

class ListType(object):
    def __init__(self, tp):
        self.tp = tp
    def fromString(self, obj):
        if (not obj.startswith("[")) or (not obj.endswith("]"):
            raise ValueError("expected value to be a list")
        return list(map(lambda x:self.tp.fromString(x), ",".split(obj[1:-1])))
    def toString(self, obj):
        return "[%s]" % (",".join(map(lambda x:self.tp.toString(x), obj)))

class ProductType(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def fromString(self, obj):
        if (not obj.startswith("(")) or (not obj.endswith(")"):
            raise ValueError("expected value to be a pair")

        splt = ",".split(obj[1:-1])
        if len(splt) != 2:
            raise ValueError("expected value to be a pair")

        return (self.left.fromString(splt[0]), self.right.fromString(splt[1]))
