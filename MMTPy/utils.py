try:
    stringcls = basestring
except: 
    stringcls = str

def caseClass(name, *args):
    """
        Creates a meta-class for a scala-like case class. 
        
        name : Name of the class
        *args : Types of parameters. Use (tp) for Option[tp] and [tp] for List[tp]
    """
    class DynamicCaseClass(object):
        def __init__(self, *cargs):
            
            # check that we have the right number of arguments
            if len(cargs) != len(args):
                raise TypeError("__init__() takes %d positional argument(s) but %d were given" % (len(args) + 1, len(cargs + 1)))
            
            for (a, t) in zip(cargs, args):
                if isinstance(t, list):
                    if not isinstance(a, list):
                        raise ValueError("'%s' is not of type List[%s]" % (a, t[0]))
                    for e in a:
                        if not isinstance(e, t[0]):
                            raise ValueError("'%s' is not of type List[%s]" % (a, t[0]))
                elif isinstance(t, tuple):
                    if a != None and not isinstance(a, t[0]):
                        raise ValueError("'%s' is not of type Option[%s]" % (a, t[0]))
                else:
                    if not isinstance(a, t):
                        raise ValueError("'%s' is not of type %s" % (a, t))
            self.__classargs__ = cargs
        def __eq__(self, other):
            
            # check if the given object is an instance of this class. 
            if not isinstance(other, DynamicCaseClass):
                return False
            
            # check for all the arguments if they are the same
            for (own, other) in zip(self.__classargs__, other.__classargs__):
                if own != other:
                    return False
            
            return True
        def __repr__(self):
            arepr = ",".join(map(lambda a:"%r" % a, self.__classargs__))
            return "%s(%s)" % (name, arepr)
            
        def __neq__(self, other):
            return not self.__eq__(other)
    return DynamicCaseClass