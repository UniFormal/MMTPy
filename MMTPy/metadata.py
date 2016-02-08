from MMTPy import xml

from MMTPy.paths import uri, path
from MMTPy.clsutils import caseclass, types

class MetaData(object):
    def __init__(self):
        self.metadata = []

    def toMetaDataXML(self):
        # create an element for each meta-datum
        return xml.make_element("metadata", *[d.toXML() for d in self.metadata])
    def getMeta(self, key):
        """
        Returns a meta-data item with the given key
        """
        for md in self.metadata:
            if key == md.key:
                return md
        return None


    @staticmethod
    def parseMetaDataNode(node):
        # parse the meta-data from xml for each child
        return [MetaDatum.fromXML(c) for c in node]
    @staticmethod
    def extractMetaDataXML(onode):

        # make a copy of the original node
        node = xml.copy(onode)

        # have an array of metadata
        mds = []

        # check each of the nodes if they match
        for c in node:
            (m, md) = xml.match(c, "metadata")

            # if so, remove the node and parse it
            if m:
                mds += MetaData.parseMetaDataNode(md)
                node.remove(c)

        # return that
        return (mds, node)

class MetaDatum(object):
    @staticmethod
    def fromXML(node):
        if xml.matches(node, "link"):
            return Link.fromXML(node)
        elif xml.matches(node, "tag"):
            return Tag.fromXML(node)
        elif xml.matches(node, "meta"):
            return Meta.fromXML(node)

        raise ValueError("Not a valid meta-datum")

@caseclass.caseclass
@types.argtypes(path.GlobalName, uri.URI)
class Link(MetaDatum):
    def __init__(self, key, u):
        super(Link, self).__init__()

        self.key = key
        self.uri = u
    def toXML(self):
        return xml.make_element("link", rel=self.key, resource=self.uri)
    @staticmethod
    def fromXML(node):
        if not xml.matches(node, "link"):
            raise ValueError("not a valid Link")

        # parse uri and key
        key = path.Path.parse(node.attrib.get("rel"))

        u = uri.URI.parse(node.attrib.get("resource"))

        # and create a link object
        return Link(key, u)

@caseclass.caseclass
@types.argtypes(path.GlobalName)
class Tag(MetaDatum):
    def __init__(self, key):
        super(Tag, self).__init__()

        self.key = key
    def toXML(self):
        return xml.make_element("tag", property=self.key)
    @staticmethod
    def fromXML(node):
        if not xml.matches(node, "tag"):
            raise ValueError("not a valid tag")

        # parse key
        key = path.Path.parse(node.attrib.get("property"))

        # and create a link object
        return Tag(key)

@caseclass.caseclass
@types.argtypes(path.GlobalName, object)
class Meta(MetaDatum):
    def __init__(self, key, value):
        super(Meta, self).__init__()

        self.key = key
        self.value = value
    def toXML(self):
        return xml.make_element("meta", self.value.toOBJXML(), property=self.key)
    @staticmethod
    def fromXML(node):
        if not xml.matches(node, "meta"):
            raise ValueError("not a valid Meta")

        # parse key and value
        key = path.Path.parse(node.attrib.get("property"))

        from MMTPy.content.objects.terms import term
        value = term.Term.fromXML(node[0])

        # and create a link object
        return Meta(key, value)
