from MMTPy import xml, metadata

from MMTPy.caseclass import caseclass
from MMTPy.objects.terms import term, omid

class OMATTR(caseclass.make(term.Term, omid.OMID, term.Term), term.Term):
    def __init__(self, arg, key, value):
        super(OMATTR, self).__init__(arg, key, value)
        self.arg = arg
        self.key = key
        self.value = value
    def toXML(self):
        return xml.make_element(xml.omt("OMATTR"),
            self.toMetaDataXML(),
            (xml.omt("OMATP"), [self.key.toXML(), self.value.toXML()]),
            self.arg.toXML()
        )

    @staticmethod
    def fromXML(onode):
        (md, node) = metadata.MetaData.extractMetaDataXML(onode)
        (m, (omattr, (omatp, (omkey, omval), omarg))) = xml.match(node,
            (xml.omt("OMATTR"),
                [
                    (xml.omt("OMATP"), [xml.omt(""), xml.omt("")]),
                    xml.omt("")
                ]
            )
        )

        if m:
            parsed = OMATTR(term.Term.__parse__(omarg), term.Term.__parse__(omkey), term.Term.__parse__(omval))
            parsed.metadata = md

            return parsed
        else:
            raise ValueError("Not a well-formed <OMATTR/>")
