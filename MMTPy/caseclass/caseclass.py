from caseclass.types import verify, verifyK

class StaticCaseClass(object):
    def __init__(self, *args, **kwargs):
        #: The name of this case class 
        self.__cc_name__ = self.__class__.__name__
        
        #: The arguments given to this case class
        self.__cc_args__ = args
        
        #: The keyword arguments given to this case class
        self.__cc_kwargs__ = kwargs
    def __eq__(self, other):
        # check if the given object  is indeed an instance of this case class
        if not isinstance(other, StaticCaseClass):
            return False

        # check if the arguments are the same
        for (own, other) in zip(self.__cc_args__, other.__cc_args__):
            if own != other:
                return False
        
        # check if the keyword arguments are the same
        for(own, other) in zip(self.__cc_kwargs__, other.__cc_kwargs__):
            if own != other:
                return False
        
        # then return if their classes are actually the same
        # so that we do not have equality based on arguments only
        return self.__class__ == other.__class__
    def __neq__(self, other):
        return not self.__eq__(other)
    def __repr__(self):
        
        # string representations of the arguments and keyword arguments
        alist = list(map(lambda a:"%r" % a, self.__cc_args__))
        kwarglist = list(map(lambda p:"%s=%r" % p, self.__cc_kwargs__.items()))
        
        # join them
        arepr = ",".join(alist+kwarglist)
        
        # and put them after the name of the class
        return "%s(%s)" % (self.__cc_name__, arepr)

def make(*args, **kwargs):
    """
    Creates a meta-class for a scala-like case class.

    name -- Name of the class
    args -- Types of parameters. Use (tp) for Option[tp] and [tp] for List[tp]
    """
    class DynamicCaseClass(StaticCaseClass):
        def __init__(self, *cargs, **kcargs):
            
            # initialise the StaticCaseClass instance
            super(DynamicCaseClass, self).__init__(*cargs, **kcargs)
            
            # check that we have the right number of arguments
            if len(cargs) != len(args):
                raise TypeError("__init__() takes %d positional argument(s) but %d were given" % (len(args) + 1, len(cargs + 1)))
            
            # check that we have the right types
            verify(cargs, args)
            verifyK(kcargs, kwargs)
            
    return DynamicCaseClass
