from MMTPy.library.lf import LF
from MMTPy.objects.terms import oma, ombindc

def lf_apply(f, *args):
    """
    Applies an lf-function to a term
    """

    return oma.OMA(~LF.apply, f, *args)

def lf_unapply(tm):
    """
    Unpacks an lf-function from a term into a pair of (f, args)
    """

    if isinstance(tm, oma.OMA):
        if tm.fun == ~LF.apply and len(tm.args) > 0:
            return (tm.args[0], tm.args[1:])
        else:
            return (tm.fun, tm.args)

    raise ValueError("not an LF-apply")

def lf_pack_function_types(pi, args, rt):
    """
    Packages an LF argument type
    """

    # start with the return type
    tm = rt

    # for each of the types, add them back
    for a in reversed(args):
        tm = (~LF.arrow)(a, tm)

    # TODO: Handle the context and OMBINDC
    if pi:
        raise NotImplementedError

    # and return it
    return tm

def lf_unpack_function_types(tm):
    """
    Unpackages an LF argument into a pair or (pi, tps)
    """

    if isinstance(tm, ombindc.OMBINDC):
        pi = {}
    else:
        pi = {}


    tps = []

    while(isinstance(tm, oma.OMA)):
        (f, args) = tm.uncall()
        if f == ~LF.arrow:
            tps.append(args[0])
            tm = args[1]
        else:
            break

    return (pi, args, tm)
