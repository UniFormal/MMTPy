from MMTPy.clsutils import caseclass, types

from MMTPy.paths import uri

from MMTPy.utils import ustr

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

class LNStep(object):
    def __init__(self):
        pass
    
    @staticmethod
    def parse(s):
        s = ustr(s)
        if s.startswith("[") and s.endswith("]"):
            return ComplexStep(Path.parseM(s[1:-1]))
        else:
            return SimpleStep(s)

@caseclass.caseclass
@types.argtypes(types.strtype)
class SimpleStep(LNStep):
    def __init__(self, name):
        LNStep.__init__(self)
        
        self.name = name
    def __str__(self):
        return self.name
    def __repr__(self):
        return "SimpleStep[%r]" % (str(self))

@caseclass.caseclass
@types.argtypes([LNStep])
class LocalName(object):
    def __init__(self, steps):
        self.steps = steps
    def __str__(self):
        return "/".join(map(ustr, self.steps))
    def __repr__(self):
        return "LocalName[%r]" % (ustr(self))
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

class Path(object):
    def __init__(self):
        pass
    
    @staticmethod
    def split(s):
        """
            Splits a path represented by a string into a tuple of
            (documentURI, moduleURI, symbolName, componentName)
        """
        # make sure the thing to split is a string
        left = ustr(s)

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
        dpath = DPath(uri.URI.parse(documentURI)) if documentURI else None
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

    def __mod__(self, other):
        """
        Adds a new component with a "?" at the end of this
        """
        return Path.parse("%s?%s" %(ustr(self), ustr(other)))

    def __div__(self, other):
        """
        Adds a new component with a "/" at the end of this
        """
        return Path.parse("%s/%s" %(ustr(self), ustr(other)))

    def __truediv__(self, other):
        """
        Same as __div__(self, other)
        """
        return self.__div__(other)

    def __getattr__(self, key):
        """
        Same as __getitem__, but might not work for all paths.
        """
        return self[key]

    def __getitem__(self, key):
        """
            Same as __mod__(self, key)
        """
        return self % key

    def __mul__(self, other):
        """
        Adds a path at the end of this
        """
        return Path.parse("%s%s" %(ustr(self), ustr(other)))

def m(base):
    """
    Alias for PathBuilder(base)
    """
    return PathBuilder(base)

@caseclass.caseclass
@types.argtypes(uri.URI)
class DPath(Path):
    def __init__(self, u):
        Path.__init__(self)
        
        self.uri = u
    def __str__(self):
        return "%s" % ustr(self.uri)
    def __repr__(self):
        return "DPath[%r]" % (ustr(self))

class ContentPath(Path):
    def toTerm(self):
        """
        Turns this ContentPath into a term by wrapping it in an OMID
        """
        from MMTPy.content.objects.terms import omid
        return omid.OMID(self)
    def __call__(self, *args, **kwargs):
        """
        Equivalent to self.toTerm().call
        """
        return self.toTerm().__call__(*args, **kwargs)
    def __invert__(self):
        """
        Alias of toTerm(self)
        """
        return self.toTerm()

@caseclass.caseclass
@types.argtypes(ContentPath, types.strtype)
class CPath(Path):
    def __init__(self, parent, component):
        Path.__init__(self)
        
        self.parent = parent
        self.component = component
    def __str__(self):
        return "%s?%s" % (self.parent, self.component)
    def __repr__(self):
        return "CPath[%r]" % (ustr(self))

@caseclass.caseclass
@types.argtypes(DPath, LocalName)
class MPath(ContentPath):
    def __init__(self, parent, name):
        ContentPath.__init__(self)
        
        self.parent = parent
        self.module = self
        self.name = name
    def toMPath(self):
        return self
    def __str__(self):
        return "%s?%s" % (self.parent, self.name)
    def __repr__(self):
        return "MPath[%r]" % (ustr(self))

@caseclass.caseclass
@types.argtypes(MPath, LocalName)
class GlobalName(ContentPath):
    def __init__(self, module, name):
        ContentPath.__init__(self)
        
        self.module = module
        self.name = name
    def __str__(self):
        return "%s?%s" % (self.module, self.name)
    def __repr__(self):
        return "GlobalName[%r]" % (ustr(self))

@caseclass.caseclass
@types.argtypes(MPath)
class ComplexStep(LNStep):
    def __init__(self, path):
        LNStep.__init__(self)
        
        self.path = path
    def __str__(self):
        return "[%s]" % self.path
    def __repr__(self):
        return "ComplexStep[%r]" % (ustr(self))