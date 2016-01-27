from MMTPy.specific.lf import LF
from MMTPy.objects.terms import oma

def lf_apply(f, args):
    return oma.OMA(LF.apply, f, args)
def lf_unapply(f, args):
    return oma.OMA()
