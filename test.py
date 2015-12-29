from MMTPy.objects.path import SimpleStep, LocalName, DPath, MPath, GlobalName
from MMTPy.objects.URI import URI
from MMTPy.objects.term import OMID

m1 = MPath(DPath(URI.fromstring("helloworld")), LocalName([SimpleStep("f")]))
m2 = MPath(DPath(URI.fromstring("helloworld")), LocalName([SimpleStep("f")]))
m3 = MPath(DPath(URI.fromstring("hello")), LocalName([SimpleStep("f")]))
idp = OMID(m3)

print(m1)
print(m2)
print(m3)
print(idp)
print(m1 == m2) # True
print(m1 == m3) # False

