#!/usr/bin/env python
# -*- coding: utf-8 -*-

from MMTPy.objects import path
from MMTPy.connection import qmtclient
from MMTPy.library.lf import wrappers
from MMTPy.declarations import declaration

# Create a client to connect to MMT
q = qmtclient.QMTClient("http://localhost:8080/")

# This is the namespace of the LATIN Math library
latin_math = path.Path.parse("http://latin.omdoc.org")/"math"

# We will now retrieve the types of an operation within that archive

# build the path to the constant, in this case "∘", and request its type via MMT
op_tp = q.getType(latin_math.Magma[u"∘"])

# next we can unpack this function type into a triple of
#(Type Variables, argument types, return type)
(op_bd, op_tps, op_rt) = wrappers.lf_unpack_function_types(op_tp)

# op_tp_p = wrappers.lf_pack_function_types(op_bd, op_tps, op_rt)

# we now do the same for something which actually has Type Variables
sym_tp = q.getType(latin_math.Symmetric.sym)
(sym_bd, sym_tps, sym_rt) = wrappers.lf_unpack_function_types(sym_tp)
