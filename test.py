from MMTPy.objects.path import Path

s1 = Path.parseS("http://cds.omdoc.org/urtheories?example?[http://cds.omdoc.org/urtheories?examples]")
s2 = Path.parseS("http://cds.omdoc.org/urtheories?example?[http://cds.omdoc.org/urtheories?examples]/2/3")
print(s1)
print(s2)
print(s2 == Path.parseS(s1))