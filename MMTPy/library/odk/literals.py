from MMTPy.literals import realization, semantic
from MMTPy.library.odk import ODK

ctx = realization.LiteralContext([
    realization.RealizedType(semantic.StandardBool(), ~ODK.Logic.bool),
    realization.RealizedType(semantic.StandardNat(), ~ODK.Nat.nat),
    realization.RealizedType(semantic.StandardInt(), ~ODK.Int.int),
    realization.RealizedType(semantic.StandardString(), ~ODK.Strings.string)
])
