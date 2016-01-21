def declaration(pth):
    from MMTPy.query.queries import Related, Literal
    from MMTPy.query.relationexps import ToObject
    from MMTPy.query.binary import Declares
    
    return Related(Literal(pth), ToObject(Declares()))