#!/usr/bin/env python
# -*- coding: utf-8 -*-

from MMTPy.objects import path
from MMTPy.connection import qmtclient
from MMTPy.library.lf import wrappers
from MMTPy.declarations import declaration

# init client
q = qmtclient.QMTClient("http://localhost:8080/")

# find the path to latin math
latin_math = path.Path.parse("http://latin.omdoc.org")/"math"

# function for magma type
op_tp = q.getType(latin_math.Magma[u"∘"])
(op_bd, op_tps, op_rt) = wrappers.lf_unpack_function_types(op_tp)
op_tp_p = wrappers.lf_pack_function_types(op_bd, op_tps, op_rt)

# function for symmetric type
sym_tp = q.getType(latin_math.Symmetric.sym)
(sym_bd, sym_tps, sym_rt) = wrappers.lf_unpack_function_types(sym_tp)
sym_tp_p = wrappers.lf_pack_function_types(sym_bd, sym_tps, sym_rt)
