from MMTPy.literals import realization, semantic
from MMTPy.odk import paths

ctx = realization.LiteralContext([
    realization.RealizedType(semantic.StandardBool(), ~paths.Logic_bool),
    realization.RealizedType(semantic.StandardNat(), ~paths.Nat_nat),
    realization.RealizedType(semantic.StandardInt(), ~paths.Int_int),
    realization.RealizedType(semantic.StandardString(), ~paths.Strings_string)
])
