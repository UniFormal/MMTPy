typetype = type(object) # the type of a type
typefunc = type(lambda x:x) # the funciton type

def match(o, pattern):
    """
    Checks if an object o matches a pattern. 
    
    Returns a pair of (matches, )
    """
    
    from caseclass import caseclass
    
    # for a case class, use the appropriate method
    if isinstance(o, caseclass.StaticCaseClass):
        return o.__match__(pattern)
    
    # Simple Pattern matching:
    
    # VALUE matching
    if o == pattern:
        return (True, o)
    
    # instance checking
    if isinstance(pattern, typetype):
        return (isinstance(o, pattern), o)
    
    # function checking
    if isinstance(pattern, typefunc):
        return (True if pattern(o) else False, o)
    
    # if the pattern is None, we always match
    return (pattern == None, o)