#: The type of all types
typetype = type(object)
# The type of strings
try:
    strtype = basestring
except:
    strtype = str


def verify(args, types):
    """
    Verifies types of arguments and throws an exception if they do not match.
    Returns a boolean indicating if pattern match types were used.

    args -- Arguments to check.
    types -- Types of parameters. Use (tp) for Option[tp] and [tp] for List[tp]
    """
    ispattern = False

    for (a, t) in zip(args, types):
        if isinstance(t, list):
            if not isinstance(a, list):
                raise TypeError("'%s' is not of type List[%s]" % (a, t[0]))
            for e in a:
                if not isinstance(e, t[0]):
                    raise TypeError("'%s' is not of type List[%s]" % (a, t[0]))
        elif isinstance(t, tuple):
            if a != None and not isinstance(a, t[0]):
                raise TypeError("'%s' is not of type Option[%s]" % (a, t[0]))
        else:
            if not isinstance(a, t):
                raise TypeError("'%s' is not of type %s" % (a, t))
def verifyK(args, types):
    """Same as verify(), but for dictionaries instead of lists. """

    arglist = []
    typelist = []

    # check for each of the possible types
    for key in types:
        if key in args:
            arglist.append(args[key])
            typelist.append(types[key])
        else:
            arglist.append(None)
            typelist.append(types[key])

    # if we have an argument that is unknown we can fail immediatly
    for key in args:
        if not key in types:
            raise TypeError("received unexpected keyword argument %s" % (key))

    # recurse into the list version
    verify(arglist, typelist)
