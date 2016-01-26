from MMTPy.query.queries import QueryFunctionApply, Literal

def declaration(pth):
    """
    Builds a declaration query for a given path
    """

    return QueryFunctionApply("presentDecl", Literal(pth), ["xml"])

def presentation(tm, frm):
    """
    Builds a presentation query for a given term and a given format
    """
    return QueryFunctionApply("present", Literal(tm), [str(frm)])

def simplification(obj, thy):
    """
    Builds a declaration query for an object relative to a given theory
    """

    return QueryFunctionApply("simplify", Literal(obj), [str(thy)])

def parsing(s, thy):
    """
    Builds a parsing query for an string relative to a given theory
    """

    return QueryFunctionApply("parse", Literal(s), [str(thy)])

def infering(obj, fnd):
    """
    Builds an analyzing query for an object relative to a given foundation.
    """

    return QueryFunctionApply("infer", Literal(obj), [str(fnd)])

def analyzing(obj, thy):
    """
    Builds an analyzing query for an object relative to a given theory.
    """

    return QueryFunctionApply("analyze", Literal(obj), [str(thy)])
