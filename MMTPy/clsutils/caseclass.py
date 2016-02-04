from . import types

class StaticCaseClass(object):
    """
    Super class for all case classes
    """
    def __init__(self, cargs, kcwargs):
        """
        Initialises case class parameters
        """

        #: The name of this case class
        self.__cc_name__ = self.__class__.__name__

        #: The arguments given to this case class
        self.__cc_args__ = cargs

        #: The keyword arguments given to this case class
        self.__cc_kwargs__ = kcwargs
    def __uninit__(self):
        """
        Unpacks the parameters originally given to this case class.
        """
        return tuple(self.__cc_args__)
    def __eq__(self, other):
        """
        Implements equality between case classes. Two case class instances are
        equal if their parameters are equal and their classes are equal.
        """
        # check if the given object  is indeed an instance of this case class
        if not isinstance(other, StaticCaseClass):
            return False

        # if the classes are not the same, we return False
        if self.__class__ != other.__class__:
            return False

        # check if the arguments are the same
        for (ow, ot) in zip(self.__cc_args__, other.__cc_args__):
            if not (ow == ot):
                return False

        # check if the keyword arguments are the same
        for key in self.__cc_kwargs__:

            if not key in other.__cc_kwargs__:
                return False

            if self.__cc_kwargs__[key] != other.__cc_kwargs__[key]:
                return False

        return True
    def __ne__(self, other):
        return not self.__eq__(other)
    def __repr__(self):
        """
        Implements a representation for Case classes. This is given by the class
        name and the representation of all the parameters.
        """
        # string representations of the arguments and keyword arguments
        alist = list(map(lambda a:"%r" % (a), self.__cc_args__))
        kwarglist = list(map(lambda p:"%s=%r" % (p), self.__cc_kwargs__.items()))

        # join them
        arepr = ",".join(alist+kwarglist)

        # and put them after the name of the class
        return "%s[%s]" % (self.__cc_name__, arepr)

def caseclass(cls):
    """
    Class Decorator that makes a class a case class. 
    Note: This breaks super() on case-class instances. 
    """
    def __init__(self,*args,**kwargs):
        StaticCaseClass.__init__(self, args, kwargs)
        return super(tp, self).__init__(*args, **kwargs)
    
    tp = type(cls.__name__, (cls,StaticCaseClass,),{"__init__":__init__})
    return tp
