from MMTPy.objects import path
from MMTPy.connection import qmtclient

# declare all the paths to MMT
ut = path.Path.parse("http://cds.omdoc.org/urtheories")

lf = ut % "LF"
lf_pi = ut % "Pi"

# create a QMT Clienth d
q = qmtclient.QMTClient("http://localhost:8080/")

# get two definitions from the API
lf_t = q.getDeclaration(lf)
lf_pi_d = q.getDeclaration(lf_pi)
lf_pi_s = q.simplify(~lf_pi, lf)
