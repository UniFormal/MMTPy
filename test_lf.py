from MMTPy.objects import path
from MMTPy.connection import qmtclient

# declare all the paths to MMT
lf = path.Path.parse("http://cds.omdoc.org/urtheories?LF")
lf_pi = path.Path.parse("http://cds.omdoc.org/urtheories?LF?Pi")

# create a QMT Clienth d
q = qmtclient.QMTClient("http://localhost:8080/")

# get two definitions from the API
lf_t = q.getDeclaration(lf)
lf_pi_d = q.getDeclaration(lf_pi)

for t in lf_t:
    print(t)

lf_pi_t = q.simplify(lf_pi.toTerm(), lf)
