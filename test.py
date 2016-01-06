from MMTPy.objects.path import Path

s1 = Path.parseS("http://cds.omdoc.org/urtheories?example?[http://cds.omdoc.org/urtheories?examples]")
s2 = Path.parseS("http://cds.omdoc.org/urtheories?example?[http://cds.omdoc.org/urtheories?examples]/2/3")
print(s1)
print(s2)
print(s2 == Path.parseS(s1)) # should be false

from MMTPy.objects.term import Term
from MMTPy.dependencies import etree
from MMTPy import xml

sample = etree.fromstring("""
<om:OMOBJ xmlns:om="http://www.openmath.org/OpenMath">
<om:OMS base="http://cds.omdoc.org/urtheories" module="Typed" name="type">
<metadata>
<link rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/int.mmt#118.4.10:121.4.13"></link>
</metadata>
</om:OMS>
</om:OMOBJ>
""")