from MMTPy import xml

from MMTPy.objects import URI, path
from MMTPy.caseclass import caseclass

class MetaData(object):
    def __init__(self):
        self.__initmd__()
    def __initmd__(self):
        self.metadata = None
    def toMetaDataXML(self):
        # create an element for each meta-datum
        return xml.make_element("metadata", *[d.toXML() for d in self.metadata])

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
                mds.extend(MetaData.parseMetaDataNode(md))
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
class Link(caseclass.make(path.GlobalName, URI.URI), MetaDatum):
    def __init__(self, key, uri):
        super(Link, self).__init__(key, uri)
        self.key = key
        self.uri = uri
    def toXML(self):
        return xml.make_element("link", rel=self.key, resource=self.uri)
    @staticmethod
    def fromXML(node):
        if not xml.matches(node, "link"):
            raise ValueError("not a valid Link")

        # parse uri and key
        key = path.ContentPath.parseBest(node.attrib.get("rel"))

        uri = URI.URI.parse(node.attrib.get("resource"))

        # and create a link object
        return Link(key, uri)

class Tag(caseclass.make(path.GlobalName), MetaDatum):
    def __init__(self, key):
        super(Tag, self).__init__(key)
        self.key = key
    def toXML(self):
        return xml.make_element("tag", property=self.key)
    @staticmethod
    def fromXML(node):
        if not xml.matches(node, "tag"):
            raise ValueError("not a valid tag")

        # parse key
        key = path.ContentPath.parseBest(node.attrib.get("property"))

        # and create a link object
        return Tag(key)

class Meta(caseclass.make(path.GlobalName, object), MetaDatum):
    def __init__(self, key, value):
        super(Meta, self).__init__(key, uri)
        self.key = key
        self.value = value
    def toXML(self):
        return xml.make_element("meta", self.value.toOBJXML(), property=self.key)
    @staticmethod
    def fromXML(node):
        if not xml.matches(node, "meta"):
            raise ValueError("not a valid Meta")

        # parse key and value
        key = path.ContentPath.parseBest(node.attrib.get("property"))

        from MMTPy.objects.terms import term
        value = term.Term.fromXML(node[0])

        # and create a link object
        return Meta(key, value)
