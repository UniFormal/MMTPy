from MMTPy.objects import path
from MMTPy.connection import qmtclient

from MMTPy.odk import literals, codecs, paths

# paths to the elliptic curves
lmfdb_elliptic_curves = path.Path.parse("http://www.lmfdb.org/db/elliptic_curves?curves")
odk_elliptic_curves_11a1 = lmfdb_elliptic_curves % "11a1"
odk_elliptic_curves_35a2 = lmfdb_elliptic_curves % "35a2"

# create a QMT Clienth
q = qmtclient.QMTClient("http://localhost:8080/")

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
(f2, args2) = o1l.uncall(lf=True)


# we want to have a certain codec
sl_si = q.parse("standardList(standardInt)", paths.Codecs)

# get the implementation
sl_si_codec = codecs.ctx.get(sl_si)

# and decode them
ainvs_11a1 = sl_si_codec.decode(args1[5].vd.df)
ainvs_35a2 = sl_si_codec.decode(args2[5].vd.df)
