from MMTPy.objects import path
from MMTPy.connection import qmtclient

from MMTPy.literals import realization, semantic

# have a bunch of paths
import test_paths as paths

# create a QMT Clienth
q = qmtclient.QMTClient("http://localhost:8080/")

# get two definitions from the API
o1 = q.getDefinition(paths.odk_elliptic_curves_11a1)
o2 = q.getDefinition(paths.odk_elliptic_curves_35a2)

# and simplify them
o1s = q.simplify(o1, paths.lmfdb_elliptic_curves)
o2s = q.simplify(o2, paths.lmfdb_elliptic_curves)

# the literals we have
omfdb_lit = realization.RealizedContext([
    realization.RealizedType(semantic.StandardBool(), ~paths.bl),
    realization.RealizedType(semantic.StandardNat(), ~paths.nat),
    realization.RealizedType(semantic.StandardInt(), ~paths.it),
    realization.RealizedType(semantic.StandardString(), ~paths.string)
])

o1l = omfdb_lit.applyR(o1)
o2l = omfdb_lit.applyR(o2)
