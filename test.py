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


from MMTPy.declarations import theory, view

sample2 = etree.fromstring("""
<theory name="LF" base="http://cds.omdoc.org/urtheories">
  <metadata>
    <link
    rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/urtheories/lf.mmt#382.19.0:393.19.11">
</link>
    <link
    rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/urtheories/lf.mmt#382.19.0:1198.43.1">
</link>
  </metadata>
  <import from="http://cds.omdoc.org/urtheories?Typed">
    <metadata>
      <link
      rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/urtheories/lf.mmt#397.20.3:412.20.18">
</link>
    </metadata>
  </import>
  <constant name="Pi">
    <metadata>
      <link
      rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/urtheories/lf.mmt#420.22.3:453.22.36">
</link>
    </metadata>
    <notations>
      <notation dimension="1" precedence="-10000" fixity="mixfix" arguments="{ V1T,... } 2">
        <scope languages="" priority="0"/>
      </notation>
    </notations>
  </constant>
  <constant name="lambda">
    <metadata>
      <link
      rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/urtheories/lf.mmt#457.23.3:490.23.36">
</link>
    </metadata>
    <notations>
      <notation dimension="1" precedence="-10000" fixity="mixfix" arguments="[ V1T,... ] 2">
        <scope languages="" priority="0"/>
      </notation>
    </notations>
  </constant>
  <constant name="apply">
    <metadata>
      <link
      rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/urtheories/lf.mmt#494.24.3:524.24.33">
</link>
    </metadata>
    <notations>
      <notation dimension="1" precedence="-10" fixity="mixfix" arguments="1%w...">
        <scope languages="" priority="0"/>
      </notation>
    </notations>
  </constant>
  <constant name="arrow">
    <metadata>
      <link
      rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/urtheories/lf.mmt#528.25.3:561.25.36">
</link>
    </metadata>
    <notations>
      <notation dimension="1" precedence="-9990" fixity="mixfix" arguments="1->...">
        <scope languages="" priority="0"/>
      </notation>
    </notations>
  </constant>
  <ruleconstant name="info.kwarc.mmt.lf.PiType"/>
  <ruleconstant name="info.kwarc.mmt.lf.PiTerm"/>
  <ruleconstant name="info.kwarc.mmt.lf.ApplyTerm"/>
  <ruleconstant name="info.kwarc.mmt.lf.LambdaTerm"/>
  <ruleconstant name="info.kwarc.mmt.lf.Beta"/>
  <ruleconstant name="info.kwarc.mmt.lf.Extensionality"/>
  <ruleconstant name="info.kwarc.mmt.lf.PiCongruence"/>
  <ruleconstant name="info.kwarc.mmt.lf.LambdaCongruence"/>
  <ruleconstant name="info.kwarc.mmt.lf.Solve"/>
  <ruleconstant name="info.kwarc.mmt.lf.SolveType"/>
  <ruleconstant name="info.kwarc.mmt.lf.ExpandArrow"/>
  <ruleconstant name="info.kwarc.mmt.lf.TheoryTypeWithLF"/>
  <ruleconstant name="info.kwarc.mmt.lf.UnsafeBeta"/>
  <ruleconstant name="info.kwarc.mmt.lf.PiIntroduction"/>
  <ruleconstant name="info.kwarc.mmt.lf.ForwardPiElimination"/>
  <ruleconstant name="info.kwarc.mmt.lf.BackwardPiElimination"/>
</theory>
""")

sample3 = etree.fromstring("""

<view
from="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final?Monad" to="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final?List" name="ListMonad" base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final">
  <metadata>
    <link
    rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#2083.70.0:2276.78.1">
</link>
  </metadata>
  <constant
  name="[http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final?Monad]/operator">
    <metadata>
      <link
      rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#2121.71.2:2137.71.18">
</link>
    </metadata>
    <type>
      <om:OMOBJ xmlns:om="http://www.openmath.org/OpenMath">
        <om:OMA>
          <metadata>
            <link
            rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#1721.61.12:1727.61.18">
</link>
          </metadata>
          <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="arrow"></om:OMS>
          <om:OMS
          base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="Types" name="tp">
</om:OMS>
          <om:OMS
          base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="Types" name="tp">
            <metadata>
              <link
              rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#1726.61.17:1727.61.18">
</link>
            </metadata>
</om:OMS>
        </om:OMA>
      </om:OMOBJ>
    </type>
    <definition>
      <om:OMOBJ xmlns:om="http://www.openmath.org/OpenMath">
        <om:OMS
        base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="List" name="list">
          <metadata>
            <link
            rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#2132.71.13:2135.71.16">
</link>
          </metadata>
</om:OMS>
      </om:OMOBJ>
    </definition>
</constant>
  <constant name="[http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final?Monad]/unit">
    <metadata>
      <link
      rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#2140.72.2:2161.72.23">
</link>
    </metadata>
    <type>
      <om:OMOBJ xmlns:om="http://www.openmath.org/OpenMath">
        <om:OMBIND>
          <metadata>
            <link
            rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#1753.62.9:1769.62.25">
</link>
          </metadata>
          <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="Pi"></om:OMS>
          <om:OMBVAR>
            <om:OMV name="A">
              <metadata>
                <tag property="http://cds.omdoc.org/mmt?mmt?inferred-type"/>
                <link
                rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#1754.62.10:1754.62.10">
</link>
              </metadata>
              <type>
                <om:OMS
                base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="Types" name="tp">
</om:OMS>
              </type>
            </om:OMV>
          </om:OMBVAR>
          <om:OMA>
            <metadata>
              <link
              rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#1757.62.13:1769.62.25">
</link>
            </metadata>
            <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="arrow"></om:OMS>
            <om:OMA>
              <metadata>
                <link
                rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#1757.62.13:1760.62.16">
</link>
              </metadata>
              <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="apply"></om:OMS>
              <om:OMS
              base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="Types" name="tm">
</om:OMS>
              <om:OMV name="A"></om:OMV>
            </om:OMA>
            <om:OMA>
              <metadata>
                <link
                rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#1764.62.20:1769.62.25">
</link>
              </metadata>
              <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="apply"></om:OMS>
              <om:OMS
              base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="Types" name="tm">
</om:OMS>
              <om:OMA>
                <metadata>
                  <link
                  rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#1767.62.23:1769.62.25">
</link>
                </metadata>
                <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="apply"></om:OMS>
                <om:OMS
                base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="List" name="list">
                  <metadata>
                    <link
                    rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#2132.71.13:2135.71.16">
</link>
                  </metadata>
</om:OMS>
                <om:OMV name="A">
                  <metadata>
                    <link
                    rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#1769.62.25:1769.62.25">
</link>
                  </metadata>
                </om:OMV>
              </om:OMA>
            </om:OMA>
          </om:OMA>
        </om:OMBIND>
      </om:OMOBJ>
    </type>
    <definition>
      <om:OMOBJ xmlns:om="http://www.openmath.org/OpenMath">
        <om:OMBIND>
          <metadata>
            <link
            rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#2147.72.9:2159.72.21">
</link>
          </metadata>
          <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="lambda"></om:OMS>
          <om:OMBVAR>
            <om:OMV name="A">
              <metadata>
                <tag property="http://cds.omdoc.org/mmt?mmt?inferred-type"/>
                <link
                rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#2148.72.10:2148.72.10">
</link>
              </metadata>
              <type>
                <om:OMS
                base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="Types" name="tp">
</om:OMS>
              </type>
            </om:OMV>
          </om:OMBVAR>
          <om:OMBIND>
            <metadata>
              <link
              rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#2151.72.13:2159.72.21">
</link>
            </metadata>
            <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="lambda"></om:OMS>
            <om:OMBVAR>
              <om:OMV name="x">
                <metadata>
                  <tag property="http://cds.omdoc.org/mmt?mmt?inferred-type"/>
                  <link
                  rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#2152.72.14:2152.72.14">
</link>
                </metadata>
                <type>
                  <om:OMA>
                    <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="apply"></om:OMS>
                    <om:OMS
                    base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="Types" name="tm">
</om:OMS>
                    <om:OMV name="A"></om:OMV>
                  </om:OMA>
                </type>
              </om:OMV>
            </om:OMBVAR>
            <om:OMA>
              <metadata>
                <link
                rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#2155.72.17:2159.72.21">
</link>
              </metadata>
              <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="apply"></om:OMS>
              <om:OMS
              base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="List" name="cons">
</om:OMS>
              <om:OMV name="A"></om:OMV>
              <om:OMV name="x">
                <metadata>
                  <link
                  rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#2155.72.17:2155.72.17">
</link>
                </metadata>
              </om:OMV>
              <om:OMA>
                <metadata>
                  <link
                  rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#2157.72.19:2159.72.21">
</link>
                </metadata>
                <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="apply"></om:OMS>
                <om:OMS
                base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="List" name="nilOf">
</om:OMS>
                <om:OMV name="A"></om:OMV>
              </om:OMA>
            </om:OMA>
          </om:OMBIND>
        </om:OMBIND>
      </om:OMOBJ>
    </definition>
  </constant>
  <constant name="[http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final?Monad]/bind">
    <metadata>
      <link
      rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#2164.73.2:2204.73.42">
</link>
    </metadata>
    <type>
      <om:OMOBJ xmlns:om="http://www.openmath.org/OpenMath">
        <om:OMBIND>
          <metadata>
            <link
            rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#1792.63.9:1827.63.44">
</link>
          </metadata>
          <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="Pi"></om:OMS>
          <om:OMBVAR>
            <om:OMV name="A">
              <metadata>
                <tag property="http://cds.omdoc.org/mmt?mmt?inferred-type"/>
                <link
                rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#1793.63.10:1793.63.10">
</link>
              </metadata>
              <type>
                <om:OMS
                base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="Types" name="tp">
</om:OMS>
              </type>
            </om:OMV>
            <om:OMV name="B">
              <metadata>
                <tag property="http://cds.omdoc.org/mmt?mmt?inferred-type"/>
                <link
                rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#1795.63.12:1795.63.12">
</link>
              </metadata>
              <type>
                <om:OMS
                base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="Types" name="tp">
</om:OMS>
              </type>
            </om:OMV>
          </om:OMBVAR>
          <om:OMA>
            <metadata>
              <link
              rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#1798.63.15:1827.63.44">
</link>
            </metadata>
            <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="arrow"></om:OMS>
            <om:OMA>
              <metadata>
                <link
                rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#1798.63.15:1803.63.20">
</link>
              </metadata>
              <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="apply"></om:OMS>
              <om:OMS
              base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="Types" name="tm">
</om:OMS>
              <om:OMA>
                <metadata>
                  <link
                  rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#1801.63.18:1803.63.20">
</link>
                </metadata>
                <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="apply"></om:OMS>
                <om:OMS
                base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="List" name="list">
                  <metadata>
                    <link
                    rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#2132.71.13:2135.71.16">
</link>
                  </metadata>
</om:OMS>
                <om:OMV name="A">
                  <metadata>
                    <link
                    rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#1803.63.20:1803.63.20">
</link>
                  </metadata>
                </om:OMV>
              </om:OMA>
            </om:OMA>
            <om:OMA>
              <metadata>
                <link
                rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#1807.63.24:1818.63.35">
</link>
              </metadata>
              <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="apply"></om:OMS>
              <om:OMS
              base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="Types" name="tm">
</om:OMS>
              <om:OMA>
                <metadata>
                  <link
                  rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#1810.63.27:1818.63.35">
</link>
                </metadata>
                <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="apply"></om:OMS>
                <om:OMS
                base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="STT" name="fun">
</om:OMS>
                <om:OMV name="A"></om:OMV>
                <om:OMA>
                  <metadata>
                    <link
                    rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#1815.63.32:1817.63.34">
</link>
                  </metadata>
                  <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="apply"></om:OMS>
                  <om:OMS
                  base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="List" name="list">
                    <metadata>
                      <link
                      rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#2132.71.13:2135.71.16">
</link>
                    </metadata>
</om:OMS>
                  <om:OMV name="B">
                    <metadata>
                      <link
                      rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#1817.63.34:1817.63.34">
</link>
                    </metadata>
                  </om:OMV>
                </om:OMA>
              </om:OMA>
            </om:OMA>
            <om:OMA>
              <metadata>
                <link
                rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#1822.63.39:1827.63.44">
</link>
              </metadata>
              <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="apply"></om:OMS>
              <om:OMS
              base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="Types" name="tm">
</om:OMS>
              <om:OMA>
                <metadata>
                  <link
                  rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#1825.63.42:1827.63.44">
</link>
                </metadata>
                <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="apply"></om:OMS>
                <om:OMS
                base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="List" name="list">
                  <metadata>
                    <link
                    rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#2132.71.13:2135.71.16">
</link>
                  </metadata>
</om:OMS>
                <om:OMV name="B">
                  <metadata>
                    <link
                    rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#1827.63.44:1827.63.44">
</link>
                  </metadata>
                </om:OMV>
              </om:OMA>
            </om:OMA>
          </om:OMA>
        </om:OMBIND>
      </om:OMOBJ>
    </type>
    <definition>
      <om:OMOBJ xmlns:om="http://www.openmath.org/OpenMath">
        <om:OMBIND>
          <metadata>
            <link
            rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#2171.73.9:2202.73.40">
</link>
          </metadata>
          <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="lambda"></om:OMS>
          <om:OMBVAR>
            <om:OMV name="A">
              <metadata>
                <tag property="http://cds.omdoc.org/mmt?mmt?inferred-type"/>
                <link
                rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#2172.73.10:2172.73.10">
</link>
              </metadata>
              <type>
                <om:OMS
                base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="Types" name="tp">
</om:OMS>
              </type>
            </om:OMV>
            <om:OMV name="B">
              <metadata>
                <tag property="http://cds.omdoc.org/mmt?mmt?inferred-type"/>
                <link
                rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#2174.73.12:2174.73.12">
</link>
              </metadata>
              <type>
                <om:OMS
                base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="Types" name="tp">
</om:OMS>
              </type>
            </om:OMV>
          </om:OMBVAR>
          <om:OMBIND>
            <metadata>
              <link
              rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#2176.73.14:2202.73.40">
</link>
            </metadata>
            <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="lambda"></om:OMS>
            <om:OMBVAR>
              <om:OMV name="l">
                <metadata>
                  <tag property="http://cds.omdoc.org/mmt?mmt?inferred-type"/>
                  <link
                  rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#2177.73.15:2177.73.15">
</link>
                </metadata>
                <type>
                  <om:OMA>
                    <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="apply"></om:OMS>
                    <om:OMS
                    base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="Types" name="tm">
</om:OMS>
                    <om:OMA>
                      <metadata>
                        <link
                        rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#1801.63.18:1803.63.20">
</link>
                      </metadata>
                      <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="apply"></om:OMS>
                      <om:OMS
                      base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="List" name="list">
</om:OMS>
                      <om:OMV name="A">
                        <metadata>
                          <link
                          rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#1803.63.20:1803.63.20">
</link>
                        </metadata>
                      </om:OMV>
                    </om:OMA>
                  </om:OMA>
                </type>
              </om:OMV>
              <om:OMV name="f">
                <metadata>
                  <tag property="http://cds.omdoc.org/mmt?mmt?inferred-type"/>
                  <link
                  rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#2179.73.17:2179.73.17">
</link>
                </metadata>
                <type>
                  <om:OMA>
                    <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="apply"></om:OMS>
                    <om:OMS
                    base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="Types" name="tm">
</om:OMS>
                    <om:OMA>
                      <metadata>
                        <link
                        rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#1810.63.27:1818.63.35">
</link>
                      </metadata>
                      <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="apply"></om:OMS>
                      <om:OMS
                      base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="STT" name="fun">
</om:OMS>
                      <om:OMV name="A"></om:OMV>
                      <om:OMA>
                        <metadata>
                          <link
                          rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#1815.63.32:1817.63.34">
</link>
                        </metadata>
                        <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="apply"></om:OMS>
                        <om:OMS
                        base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="List" name="list">
</om:OMS>
                        <om:OMV name="B">
                          <metadata>
                            <link
                            rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#1817.63.34:1817.63.34">
</link>
                          </metadata>
                        </om:OMV>
                      </om:OMA>
                    </om:OMA>
                  </om:OMA>
                </type>
              </om:OMV>
            </om:OMBVAR>
            <om:OMA>
              <metadata>
                <link
                rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#2182.73.20:2202.73.40">
</link>
              </metadata>
              <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="apply"></om:OMS>
              <om:OMA>
                <metadata>
                  <link
                  rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#2182.73.20:2192.73.30">
</link>
                </metadata>
                <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="apply"></om:OMS>
                <om:OMS
                base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="List" name="flatten">
                  <metadata>
                    <link
                    rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#2183.73.21:2189.73.27">
</link>
                  </metadata>
</om:OMS>
                <om:OMV name="B">
                  <metadata>
                    <link
                    rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#2191.73.29:2191.73.29">
</link>
                  </metadata>
                </om:OMV>
              </om:OMA>
              <om:OMA>
                <metadata>
                  <link
                  rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#2194.73.32:2202.73.40">
</link>
                </metadata>
                <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="apply"></om:OMS>
                <om:OMS
                base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="List" name="map">
</om:OMS>
                <om:OMV name="A"></om:OMV>
                <om:OMA>
                  <om:OMS base="http://cds.omdoc.org/urtheories" module="LF" name="apply"></om:OMS>
                  <om:OMS
                  base="http://foswiki.cs.uu.nl/foswiki/IFIP21/Goteborg/MMT-tutorial-final" module="List" name="list">
</om:OMS>
                  <om:OMV name="B">
                    <metadata>
                      <link
                      rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#1817.63.34:1817.63.34">
</link>
                    </metadata>
                  </om:OMV>
                </om:OMA>
                <om:OMV name="f">
                  <metadata>
                    <link
                    rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#2199.73.37:2199.73.37">
</link>
                  </metadata>
                </om:OMV>
                <om:OMV name="l">
                  <metadata>
                    <link
                    rel="http://cds.omdoc.org/mmt?metadata?sourceRef" resource="http://docs.omdoc.org/examples/IFIP21_tutorial.mmt#2201.73.39:2201.73.39">
</link>
                  </metadata>
                </om:OMV>
              </om:OMA>
            </om:OMA>
          </om:OMBIND>
        </om:OMBIND>
      </om:OMOBJ>
    </definition>
  </constant>
</view>
""")

from MMTPy import connection
from MMTPy.objects import path

lf = path.Path.parseBest("http://cds.omdoc.org/urtheories?LF")

c = connection.Connection("http://localhost:8080/")
