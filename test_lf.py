#!/usr/bin/env python
# -*- coding: utf-8 -*-

from MMTPy.bridge import bridge

# Create a new Namespace Bridge()
ns = bridge.Bridge.create("http://localhost:8080/", "http://latin.omdoc.org/math")

# get the magma theory
magma_theory = ns.getTheory("Magma")

# get the types of the circle operator
magma_op_type = magma_theory.getDeclaration(u"∘").getType()
magma_op_args = magma_op_type.getArgumentTypes()
magma_op_return = magma_op_type.getReturnType()

# get the universe type - this is the same throughout http://latin.omdoc.org/math
universe_type = ns.getTheory("Universe").getDeclaration("u").toTerm()

# check if the return type is actually the universe
op_returns_universe = (universe_type == magma_op_return)
