from MMTPy.objects import path
from MMTPy.connection import qmtclient

# declare all the paths to MMT
lf = path.Path.parse("http://cds.omdoc.org/urtheories?LF")
lf_pi = path.Path.parse("http://cds.omdoc.org/urtheories?LF?Pi")
odk_elliptic_curves = path.Path.parse("http://www.lmfdb.org/?elliptic_curves")
odk_elliptic_curves_35a2 = path.Path.parse("http://www.lmfdb.org/?elliptic_curves?35a2")
odk_elliptic_curves_11a1 = path.Path.parse("http://www.lmfdb.org/?elliptic_curves?11a1")

# create a QMT Client
q = qmtclient.QMTClient("http://localhost:8080/")

# get two definitions from the API
o1 = q.getDefinition(odk_elliptic_curves_35a2)
o2 = q.getDefinition(odk_elliptic_curves_11a1)

# and simplify them
o1s = q.simplify(o1, odk_elliptic_curves)
o2s = q.simplify(o2, odk_elliptic_curves)
