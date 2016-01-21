def declaration(pth):
    """
    Builds a declaration query for a given path
    """
    from MMTPy.query.queries import QueryFunctionApply, Literal
    return QueryFunctionApply("presentDecl", Literal(pth), ["xml"])