from MMTPy.objects import path

# declare all the paths to MMT
ODK_path = path.Path.parse("http://www.opendreamkit.org/")
lmfdb_elliptic_curves = path.Path.parse("http://www.lmfdb.org/db/elliptic_curves?curves")

# lots and lots of paths
typesystem = ODK_path % "Types"
logic = ODK_path % "Logic"
natliterals = ODK_path % "Nat"
intliterals = ODK_path % "Int"
strings = ODK_path % "Strings"
lists = ODK_path % "Lists"
vectors = ODK_path % "Vectors"

tm = typesystem % "tm"
bl = logic % "bool"
tt = logic % "true"
ff = logic % "false"
it = intliterals % "int"
nat = natliterals % "nat"
succ = natliterals % "nat_succ"
string = strings % "string"
lt = lists % "list"
nil = lists % "nil"
cons = lists % "cons"
vector = vectors % "vector"
zerovec = vectors % "zerovec"
vectorprepend = vectors % "vector_prepend"

odk_elliptic_curves_11a1 = lmfdb_elliptic_curves % "11a1"
odk_elliptic_curves_35a2 = lmfdb_elliptic_curves % "35a2"
