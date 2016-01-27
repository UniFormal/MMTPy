from MMTPy.objects import path
from MMTPy.connection import qmtclient
from MMTPy.library.lf import wrappers

# init client
q = qmtclient.QMTClient("http://localhost:8080/")

# paths
latin_math = path.Path.parse("http://latin.omdoc.org")/"math"
magma_op = latin_math.Magma["∘"]

# get the type of the operation itself
op_tp = q.getType(magma_op)

(bd, tps, rt) = wrappers.lf_unpack_function_types(op_tp)
op_tp_p = wrappers.lf_pack_function_types(bd, tps, rt)
