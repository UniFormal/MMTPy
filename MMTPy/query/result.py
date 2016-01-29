from MMTPy import xml
from MMTPy.caseclass import caseclass

class Result(object):
    def __init__(self, objects, auto = True):
        self.objects = objects
    def __getitem__(self, key):
        return self.objects.__getitem__(key)
    def __len__(self):
        return len(self.objects)
    def __iter__(self):
        for o in self.objects:
            yield o
    def __str__(self):
        return str(self.objects)
    def __repr__(self):
        return "Result%r" % (self.objects)

    @staticmethod
    def fromXML(node, auto = True):
        if xml.matches(node, "{http://www.w3.org/1999/xhtml}div"):
            return Result([Error.fromXML(node)])
        elif xml.matches(node, "results"):
            return Result([Result.fromSingleXML(c[0], auto=auto) for c in node])
        elif xml.matches(node, "result"):
            return Result([Result.fromSingleXML(node[0], auto=auto)])
        else:
            raise ValueError("not a valid <results/>")


    @staticmethod
    def fromSingleXML(node, auto=True):

        if xml.matches(node, "uri"):
            from MMTPy.paths import path
            return path.Path.parse(node.attrib.get("path"))
        elif xml.matches(node, "object"):
            from MMTPy.objects import obj
            return obj.Obj.fromXML(node[0])
        elif xml.matches(node, "xml"):

            if auto:

                try:
                    from MMTPy.objects import obj
                    return obj.Obj.fromXML(node[0])
                except ValueError:
                    pass
                try:
                    from MMTPy.declarations import declaration
                    return declaration.Declaration.fromXML(node[0])
                except ValueError:
                    pass

            return node[0]
        elif xml.matches(node, "string"):
            return node.text
        else:
            raise ValueError("not a valid <result>")

class Error(object):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
    def __repr__(self):
        return "Error[%r]" % self.msg

    @staticmethod
    def fromXML(node):
        from MMTPy.dependencies import etree
        return Error(xml.textcontent(node))
