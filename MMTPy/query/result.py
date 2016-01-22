from MMTPy import xml
from MMTPy.caseclass import caseclass

class Result(object):
    def __init__(self, objects):
        self.objects = objects
    def __getitem__(self, key):
        return self.objects.__getitem__(key)
    def __len__(self, key):
        return len(self.objects)
    def __iter__(self):
        for o in self.objects:
            yield o
    def __str__(self):
        return str(self.objects)
    def __repr__(self):
        return "Result%r" % (self.objects)

    @staticmethod
    def fromXML(node):
        if xml.matches(node, "results"):
            return Result([Result.fromSingleXML(c[0]) for c in node])
        elif xml.matches(node, "result"):
            return Result([Result.fromSingleXML(node[0])])
        else:
            raise ValueError("not a valid <results/>")


    @staticmethod
    def fromSingleXML(node):

        if xml.matches(node, "uri"):
            from MMTPy.objects import path
            return path.parseBest(node.attrib.get("path"))
        elif xml.matches(node, "object"):
            from MMTPy.objects import obj
            return obj.Obj.fromXML(node[0])
        elif xml.matches(node, "xml"):
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
