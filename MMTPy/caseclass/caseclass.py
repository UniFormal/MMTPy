from . import types

class StaticCaseClass(object):
    """
    Generic case class Implementation
    """
    def __init__(self, cargs, kcwargs):
        #: The name of this case class
        self.__cc_name__ = self.__class__.__name__

        #: The arguments given to this case class
        self.__cc_args__ = cargs

        #: The keyword arguments given to this case class
        self.__cc_kwargs__ = kcwargs

        #: Indiciator if this class is a pattern that can be pattern matched.
        # should be overwritten by any subclass
        self.__cc_pattern__ = False
    def __eq__(self, other):
        # check if the given object  is indeed an instance of this case class
        if not isinstance(other, StaticCaseClass):
            return False

        # if the classes are not the same, we return False
        if self.__class__ != other.__class__:
            return False

        # check if the arguments are the same
        for (ow, ot) in zip(self.__cc_args__, other.__cc_args__):
            if ow != ot:
                return False

        # check if the keyword arguments are the same
        for key in self.__cc_kwargs__:

            if not key in other.__cc_kwargs__:
                return False

            if self.__cc_kwargs__[key] != other.__cc_kwargs__[key]:
                return False

        return True
    def __neq__(self, other):
        return not self.__eq__(other)
    def __repr__(self):

        # string representations of the arguments and keyword arguments
        alist = list(map(lambda a:"%r" % (a), self.__cc_args__))
        kwarglist = list(map(lambda p:"%s=%r" % (p), self.__cc_kwargs__.items()))

        # join them
        arepr = ",".join(alist+kwarglist)

        # and put them after the name of the class
        return "%s(%s)" % (self.__cc_name__, arepr)

    def __matches__(self, other):
        """
        Matches this pattern against a case class instance.
        """

        # if we are not a pattern, we can simply check equality
        if not self.__cc_pattern__:
            return self == other

        from . import matching

        # check if the arguments are the same
        for (ow, ot) in zip(self.__cc_args__, other.__cc_args__):
            if not matching.match(ow, ot):
                return False

        # check if the keyword arguments are the same
        for (ow, ot) in zip(self.__cc_kwargs__, other.__cc_kwargs__):
            if not matching.match(ow, ot):
                return False

        return True

def make(*args, **kwargs):
    """
    Creates a meta-class for a scala-like case class.

    name -- Name of the class
    args -- Types of parameters. Use (tp) for Option[tp] and [tp] for List[tp]
    """


    def __init__(self, *cargs, **kcargs):

        # check that we have the right number of arguments
        if len(cargs) != len(args):
            raise TypeError("__init__() takes %d positional argument(s) but %d were given" % (len(args) + 1, len(cargs + 1)))



        # initialise the StaticCaseClass instance
        StaticCaseClass.__init__(self, cargs, kcargs)

        # check that we have the right types
        self.__cc_pattern__ = types.verify(cargs, args) or types.verifyK(kcargs, kwargs)

    return type("DynamicCaseClass", (StaticCaseClass, ), {"__init__":__init__})
