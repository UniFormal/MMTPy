from .. import utils

from . import URI

"""
    This file defines Paths for MMT. 
    
    LNStep = 
          SimpleStep (name : String)
        | ComplexStep (path : MPath)
    LocalName (steps : List[LNStep])
    Path = 
          DPath (uri : URI)
        | ContentPath
        | CPath (parent : ContentPath, component : String)
    ContentPath = 
          MPath (parent : DPath, name: LocalName)
        | GlobalName (module : MPath, name: LocalName)
"""

class LNStep(): pass

class SimpleStep(utils.caseClass("SimpleStep", utils.stringcls), LNStep):
    def __init__(self, name):
        super(SimpleStep, self).__init__(name)
        self.name = name

class LocalName(utils.caseClass("LocalName", [LNStep])):
    def __init__(self, steps):
        super(LocalName, self).__init__(steps)
        self.steps = steps

class Path(): pass

class DPath(utils.caseClass("DPath", URI.URI), Path):
    def __init__(self, uri):
        super(DPath, self).__init__(uri)
        self.uri = uri

class ContentPath(DPath): pass

class CPath(utils.caseClass("CPath", ContentPath, utils.stringcls), Path):
    def __init__(self, parent, component):
        super(CPath, self).__init__(parent, component)
        self.parent = parent
        self.component = component

class MPath(utils.caseClass("MPath", DPath, LocalName), ContentPath):
    def __init__(self, parent, name):
        super(MPath, self).__init__(parent, name)
        self.parent = parent
        self.name = name
        
class GlobalName(utils.caseClass("GlobalName", MPath, LocalName), ContentPath):
    def __init__(self, module, name):
        super(GlobalName, self).__init__(module, name)
        self.module = module
        self.name = name

class ComplexStep(utils.caseClass("ComplexStep", MPath), LNStep):
    def __init__(self, name):
        super(ComplexStep, self).__init__(name)