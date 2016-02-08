class CaseClass(object):
    """
    Class that implements all CaseClass methods.
    """

    def __init__(self, *cargs, **kcwargs):
        """
        Initialises case class parameters
        """

        #: The name of this case class
        self.__cc_name__ = self.__class__.__name__

        #: The arguments given to this case class
        self.__cc_args__ = cargs

        #: The keyword arguments given to this case class
        self.__cc_kwargs__ = kcwargs

        # return the new instance
        return self
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
        if not isinstance(other, CaseClass):
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
        return "%s(%s)" % (self.__cc_name__, arepr)

def caseclass(cls):
    """
    Class Decorator the makes a class a CaseClass
    """

    # get the name of the super class
    name = cls.__name__

    # get the super classes of the wrapped class
    mro = cls.__bases__

    # insert the case class as a dependency. If the class inhits form object we
    # need a work around so that we have a proper mro, i. e. we replace the
    # object inheritance by inheritance from CaseClass
    if object in mro:
        idx = mro.index(object)

        mro = mro[:idx] + (CaseClass,) + mro[idx+1:]
    else:
        mro += (CaseClass,)

    # get the methods
    methods = cls.__dict__.copy()

    # we need to make sure the __init__ calls the CaseClass init
    # however we also want to call the original __init__


    # if we have an __init__ all is fine
    if "__init__" in methods:
        oldinit = methods["__init__"]

    # else we need to call the super() __init__
    else:
        def oldinit(self, *args, **kwargs):
            super(tp, self).__init__(*args, **kwargs)

    # make the actual case clas
    def __init__(self, *args, **kwargs):
        CaseClass.__init__(self, *args, **kwargs)
        return oldinit(self, *args, **kwargs)

    methods["__init__"] = __init__

    # create the new type
    tp = type(name, mro, methods)
    return tp
