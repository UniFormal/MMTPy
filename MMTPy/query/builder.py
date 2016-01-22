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
    raise NotImplementedError
    from MMTPy.query.queries import QueryFunctionApply
    return QueryFunctionApply("simplify", Literal(pth), ["xml"])
