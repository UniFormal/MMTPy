from MMTPy.objects import path
from MMTPy.connection import qmtclient


# declare all the paths to MMT
ODK_path = path.Path.parse("http://www.opendreamkit.org")
lmfdb_elliptic_curves = path.Path.parse("http://www.lmfdb.org/db/elliptic_curves?curves")

odk_elliptic_curves_11a1 = lmfdb_elliptic_curves % "11a1"
odk_elliptic_curves_35a2 = lmfdb_elliptic_curves % "35a2"

# create a QMT Clienth d
q = qmtclient.QMTClient("http://localhost:8080/")

# get two definitions from the API
o1 = q.getDefinition(odk_elliptic_curves_11a1)
o2 = q.getDefinition(odk_elliptic_curves_35a2)

# and simplify them
o1s = q.simplify(o1, lmfdb_elliptic_curves)
o2s = q.simplify(o2, lmfdb_elliptic_curves)
