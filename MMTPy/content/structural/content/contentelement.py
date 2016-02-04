from MMTPy import xml, metadata

class ContentElement(metadata.MetaData):
    def __init__(self):
        metadata.MetaData.__init__(self)
    @staticmethod
    def fromXML(node):
        if xml.matches(node, "theory") or xml.matches(node, "view"):
            from MMTPy.content.structural.content.modules import module
            return module.Module.fromXML(node)
        else:
            from MMTPy.content.structural.content.declarations import declaration
            return declaration.Declaration.fromXML(node)
