#!/usr/bin/env python
# -*- coding: utf-8 -*-

from MMTPy.bridge import bridge

# Create a new Namespace Bridge()
ns = bridge.Bridge.create("http://localhost:8080/", "http://mathhub.info/MitM/smglom/algebra")

# get the magma theory
magma_theory = ns.getTheory("magma")

# get the types of the circle operator
magma_op_type = magma_theory.getDeclaration("operation").getType()
print("magma_op_type " + str(magma_op_type))
magma_op_args = magma_op_type.getArgumentTypes()
print("magma_op_args " + str(magma_op_args))
magma_op_return = magma_op_type.getReturnType()
print("magma_op_return " + str(magma_op_return))

# get the universe type - this is the same throughout http://latin.omdoc.org/math
universe_type = ns.getTheory("Universe").getDeclaration("u").toTerm()

# check if the return type is actually the universe
op_returns_universe = (universe_type == magma_op_return)
