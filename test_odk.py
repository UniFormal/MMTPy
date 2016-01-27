from MMTPy.objects import path
from MMTPy.connection import qmtclient

from MMTPy.library.odk import literals, codecs, ODK


# create a QMT Clienth
q = qmtclient.QMTClient("http://localhost:8080/")


# paths to the elliptic curves
lmfdb_elliptic_curves = path.Path.parse("http://www.lmfdb.org/db/elliptic_curves")
odk_elliptic_curves_11a1 = lmfdb_elliptic_curves.curves["11a1"]
odk_elliptic_curves_35a2 = lmfdb_elliptic_curves.curves["35a2"]

# the curves
lmfdb_elliptic_curves_schema = path.Path.parse("http://www.lmfdb.org/schema/elliptic_curves").curves
lmfdb_elliptic_curves_schema_t = q.getDeclaration(lmfdb_elliptic_curves_schema)

# get two definitions from the API
o1 = q.getDefinition(odk_elliptic_curves_11a1)
o2 = q.getDefinition(odk_elliptic_curves_35a2)

# and simplify them
o1s = q.simplify(o1, lmfdb_elliptic_curves)
o2s = q.simplify(o2, lmfdb_elliptic_curves)

# read some of the literals, wrap them in native python objects
# and unpack the arguments
o1l = literals.ctx(o1)
(f1, args1) = o1l.uncall(lf=True)

o2l = literals.ctx(o2)
(f2, args2) = o2l.uncall(lf=True)

# try to decode stuff
o1o = codecs.ctx.decodeRecord(o1l, lmfdb_elliptic_curves_schema_t)
print(o1o)
