from MMTPy.literals import realization, semantic
from MMTPy.odk import paths

ctx = realization.LiteralContext([
    realization.RealizedType(semantic.StandardBool(), ~paths.Logic.bool),
    realization.RealizedType(semantic.StandardNat(), ~paths.Nat.nat),
    realization.RealizedType(semantic.StandardInt(), ~paths.Int.int),
    realization.RealizedType(semantic.StandardString(), ~paths.Strings.string)
])
