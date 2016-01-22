from MMTPy.caseclass import caseclass
from MMTPy.caseclass import types

from MMTPy.objects import URI

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

class LNStep():
    @staticmethod
    def parse(s):
        s = str(s)
        if s.startswith("[") and s.endswith("]"):
            return ComplexStep(Path.parseM(s[1:-1]))
        else:
            return SimpleStep(s)

class SimpleStep(caseclass.make(types.strtype), LNStep):
    def __init__(self, name):
        super(SimpleStep, self).__init__(name)
        self.name = name
    def __str__(self):
        return self.name
    def __repr__(self):
        return "SimpleStep[%s]" % (self)

class LocalName(caseclass.make([LNStep])):
    def __init__(self, steps):
        super(LocalName, self).__init__(steps)
        self.steps = steps
    def __str__(self):
        return "/".join(map(str, self.steps))
    def __repr__(self):
        return "LocalName[%s]" % (self)
    @staticmethod
    def split(s):

        # if we have the empty string, we have an empty segment
        if s == "":
            return [""]

        # if we start with a "[", we need to start a sub-segment
        # TODO: Handle sub-segments properly
        if s.startswith("["):
            try:
                idx = s.index("]")
            except ValueError:
                raise ValueError("Unclosed [ found")
            if not s[idx+1:].startswith("/"):
                return [s[:idx+1]]
            else:
                return [s[:idx+1]] + LocalName.split(s[idx+2:])
        # in the other cases we just find the next /
        else:
            try:
                idx = s.index("/")
            except ValueError:
                return [s]
            return [s[:idx]] + LocalName.split(s[idx+1:])



    @staticmethod
    def parse(s):
        """
            Parses a string into a LocalName.
        """
        # split into segments
        segments = LocalName.split(s)

        # and return that
        return LocalName(list(map(lambda s: LNStep.parse(s), segments)))

class Path():
    @staticmethod
    def split(s):
        """
            Splits a path represented by a string into a tuple of
            (documentURI, moduleURI, symbolName, componentName)
        """
        # make sure the thing to split is a string
        left = str(s)

        # have an array of return values
        comp = ["", "", "", ""] # (uri, mod, name, comp)

        # the current component
        current = 0

        # iterate character by character
        while (left != ""):
            c = left[0]

            # ? starts a new component
            if c == "?":
                if current == 3:
                    raise ValueError("MMT-URI may have at most three ?s: " + s)
                current += 1
            # there may not be #s
            elif c == "#":
                raise ValueError("MMT-URI may not have fragment: " + s)

            # we treat [s start a subcomponent
            elif c == "[" and current == 2:
                try:
                    pos = left.index("]")
                except ValueError:
                    pos = -1

                if pos == -1:
                     comp[current] += '[' # unclosed [ not treated specially
                else:
                    comp[current] += left[0:pos+1]
                    left = left[pos:] # one more character chopped below
            else:
                comp[current] += c
            left = left[1:]
        return tuple(comp)

    @staticmethod
    def __parse__(s, isSplit = False):
        """
            Parses a string representing a uri into a tuple of (dpath, mpath, spath, cpath) objects
        """

        if isSplit:
            (documentURI, moduleURI, symbolName, componentName) = s
        else:
            (documentURI, moduleURI, symbolName, componentName) = Path.split(s)

        # parse all the proper objects
        dpath = DPath(URI.URI.parse(documentURI)) if documentURI else None
        mpath = MPath(dpath, LocalName.parse(moduleURI)) if (documentURI and moduleURI) else None
        spath = GlobalName(mpath, LocalName.parse(symbolName)) if (documentURI and moduleURI and symbolName) else None
        cpath = CPath(spath if spath else mpath, componentName) if componentName else None

        # and return a tuple
        return (dpath, mpath, spath, cpath)

    @staticmethod
    def parse(s, isSplit = False):
        """
        Parses up to the deepest level possible.
        """

        (dpath, mpath, spath, cpath) = Path.__parse__(s, isSplit = isSplit)

        if cpath != None:
            return cpath
        elif spath != None:
            return spath
        elif mpath != None:
            return mpath
        else:
            return dpath



    @staticmethod
    def parseD(s, isSplit = False):
        """
            Parses a string representing a uri into a DPath or returns a value error
        """
        (dpath, mpath, spath, cpath) = Path.__parse__(s, isSplit = isSplit)

        if not dpath or mpath:
            raise ValueError("Given string does not represent a DPath. ")

        return dpath
    @staticmethod
    def parseM(s, isSplit = False):
        """
            Parses a string representing a uri into a MPath or returns a value error
        """
        (dpath, mpath, spath, cpath) = Path.__parse__(s, isSplit = isSplit)

        if not mpath or spath:
            raise ValueError("Given string does not represent a MPath. ")

        return mpath
    @staticmethod
    def parseS(s, isSplit = False):
        """
            Parses a string representing a uri into a SPath or returns a value error
        """
        (dpath, mpath, spath, cpath) = Path.__parse__(s, isSplit = isSplit)

        if not spath or cpath:
            raise ValueError("Given string does not represent a SPath. ")

        return spath
    @staticmethod
    def parseC(s, isSplit = False):
        """
            Parses a string representing a uri into a SPath or returns a value error
        """
        (dpath, mpath, spath, cpath) = Path.__parse__(s, isSplit = isSplit)

        if not cpath:
            raise ValueError("Given string does not represent a CPath. ")

        return cpath

class DPath(caseclass.make(URI.URI), Path):
    def __init__(self, uri):
        super(DPath, self).__init__(uri)
        self.uri = uri
    def __str__(self):
        return "%s" % self.uri
    def __repr__(self):
        return "DPath[%s]" % (self)

class ContentPath(DPath): pass

class CPath(caseclass.make(ContentPath, types.strtype), Path):
    def __init__(self, parent, component):
        super(CPath, self).__init__(parent, component)
        self.parent = parent
        self.component = component
    def __str__(self):
        return "%s?%s" % (self.parent, self.component)
    def __repr__(self):
        return "CPath[%s]" % (self)

class MPath(caseclass.make(DPath, LocalName), ContentPath):
    def __init__(self, parent, name):
        super(MPath, self).__init__(parent, name)
        self.parent = parent
        self.module = self
        self.name = name
    def toMPath(self):
        return self
    def __str__(self):
        return "%s?%s" % (self.parent, self.name)
    def __repr__(self):
        return "MPath[%s]" % (self)

class GlobalName(caseclass.make(MPath, LocalName), ContentPath):
    def __init__(self, module, name):
        super(GlobalName, self).__init__(module, name)
        self.module = module
        self.name = name
    def __str__(self):
        return "%s?%s" % (self.module, self.name)
    def __repr__(self):
        return "GlobalName[%s]" % (self)

class ComplexStep(caseclass.make(MPath), LNStep):
    def __init__(self, path):
        super(ComplexStep, self).__init__(path)
        self.path = path
    def __str__(self):
        return "[%s]" % self.path
    def __repr__(self):
        return "ComplexStep[%s]" % (self)
