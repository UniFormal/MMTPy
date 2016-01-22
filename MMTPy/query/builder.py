def declaration(pth):
    """
    Builds a declaration query for a given path
    """
    from MMTPy.query.queries import QueryFunctionApply, Literal
    return QueryFunctionApply("presentDecl", Literal(pth), ["xml"])

def simplification(obj, thy):
    """
    Builds a declaration query for an object relative to a given theory
    """

    from MMTPy.query.queries import QueryFunctionApply, Literal
    return QueryFunctionApply("simplify", Literal(obj), [str(thy)])

def parsing(s, thy):
    """
    Builds a parsing query for an string relative to a given theory
    """

    from MMTPy.query.queries import QueryFunctionApply, Literal
    return QueryFunctionApply("parse", Literal(s), [str(thy)])

def infering(obj, fnd):
    """
    Builds an analyzing query for an object relative to a given foundation.
    """

    from MMTPy.query.queries import QueryFunctionApply, Literal
    return QueryFunctionApply("infer", Literal(obj), [str(fnd)])

def analyzing(obj, thy):
    """
    Builds an analyzing query for an object relative to a given theory.
    """

    from MMTPy.query.queries import QueryFunctionApply, Literal
    return QueryFunctionApply("analyze", Literal(obj), [str(thy)])
