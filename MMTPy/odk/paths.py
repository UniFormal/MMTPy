from MMTPy.objects import path

ODK = path.Path.parse("http://www.opendreamkit.org/")

Types = ODK % "Types"
Logic = ODK % "Logic"
Nat = ODK % "Nat"
Int = ODK % "Int"
Strings = ODK % "Strings"
Lists = ODK % "Lists"
Vectors = ODK % "Vectors"
Codecs = ODK % "Codecs"

Types_tm = Types % "tm"

Logic_bool = Logic % "bool"
Logic_true = Logic % "true"
Logic_false = Logic % "false"

Int_int = Int % "int"
Nat_nat = Nat % "nat"
Nat_succ = Nat % "suc"

Strings_string = Strings % "string"

Lists_list = Lists % "list"
Lists_nil = Lists % "nil"
Lists_cons = Lists % "cons"

Vectors_vector = Vectors % "vector"
Vectors_zerovec = Vectors % "zerovec"
Vectors_vector_prepend = Vectors % "vector_prepend"

Codecs_standardInt = Codecs % "standardInt"
Codecs_standardString = Codecs % "standardString"
Codecs_standardBool = Codecs % "standardBool"
Codecs_boolAsInt = Codecs % "boolAsInt"
Codecs_standardList = Codecs % "standardList"
