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

from MMTPy.clsutils import types
from case_class import AbstractCaseClass, CaseClass

from MMTPy.paths import uri
from MMTPy.utils import ustr


class Path(AbstractCaseClass):
    """ Represents any Path inside MMT. """

    @staticmethod
    def split(s):
        """ Splits a path represented by a string into a tuple.

        :param s: Path to split.
        :type s: str

        :return: A tuple (documentURI, moduleURI, symbolName, componentName).
        :rtype: tuple
        """

        # TODO: Handle ComplexSteps properly and allow nested ?s

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
    def __parse(s, isSplit = False):
        """ Parses a string representing a uri into a tuple.

        :param s: String or Tuple (documentURI, moduleURI, symbolName,
        componentName) to parse.
        :type s: Any

        :param isSplit: Indicator if the path is already split.
        :type isSplit: bool

        :return: a tuple of (dpath, mpath, spath, cpath) objects
        :rtype: tuple
        """

        if isSplit:
            (documentURI, moduleURI, symbolName, componentName) = s
        else:
            (documentURI, moduleURI, symbolName, componentName) = Path.split(s)

        # parse all the proper objects
        dpath = DPath(uri.URI.parse(documentURI)) if documentURI else None
        mpath = MPath(dpath, LocalName.parse(moduleURI)) \
            if (documentURI and moduleURI) else None
        spath = GlobalName(mpath, LocalName.parse(symbolName)) \
            if (documentURI and moduleURI and symbolName) else None
        cpath = CPath(spath if spath else mpath, componentName) \
            if componentName else None

        # and return a tuple
        return dpath, mpath, spath, cpath

    @staticmethod
    def parse(s, isSplit = False):
        """ Parses a Path upto the deepest level possible.

        :param s: String or Tuple (documentURI, moduleURI, symbolName,
        componentName) to parse.
        :type s: Any

        :param isSplit: Indicator if the path is already split.
        :type isSplit: bool

        :return: a DPath, MPath, GlobalName or CPath instance.
        :rtype: Path
        """

        (dpath, mpath, spath, cpath) = Path.__parse(s, isSplit = isSplit)

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
        """ Parses a string representing a uri into a DPath instance or raises
        a ValueError.

        :param s: String or Tuple (documentURI, moduleURI, symbolName,
        componentName) to parse.
        :type s: Any

        :param isSplit: Indicator if the path is already split.
        :type isSplit: bool

        :rtype: DPath
        """

        (dpath, mpath, spath, cpath) = Path.__parse(s, isSplit = isSplit)

        if not dpath or mpath:
            raise ValueError("Given string does not represent a DPath. ")

        return dpath

    @staticmethod
    def parseM(s, isSplit = False):
        """ Parses a string representing a uri into an MPath instance or raises
            a ValueError.

        :param s: String or Tuple (documentURI, moduleURI, symbolName,
        componentName) to parse.
        :type s: Any

        :param isSplit: Indicator if the path is already split.
        :type isSplit: bool

        :rtype: MPath
        """

        (dpath, mpath, spath, cpath) = Path.__parse(s, isSplit = isSplit)

        if not mpath or spath:
            raise ValueError("Given string does not represent a MPath. ")

        return mpath

    @staticmethod
    def parseS(s, isSplit = False):
        """ Parses a string representing a uri into an GlobalName instance or
        raises a ValueError.

        :param s: String or Tuple (documentURI, moduleURI, symbolName,
        componentName) to parse.
        :type s: Any

        :param isSplit: Indicator if the path is already split.
        :type isSplit: bool

        :rtype: GlobalName
        """

        (dpath, mpath, spath, cpath) = Path.__parse(s, isSplit = isSplit)

        if not spath or cpath:
            raise ValueError("Given string does not represent a GlobalName. ")

        return spath

    @staticmethod
    def parseC(s, isSplit = False):
        """ Parses a string representing a uri into a CPath instance or
        raises a ValueError.

        :param s: String or Tuple (documentURI, moduleURI, symbolName,
        componentName) to parse.
        :type s: Any

        :param isSplit: Indicator if the path is already split.
        :type isSplit: bool

        :rtype: CPath
        """

        (dpath, mpath, spath, cpath) = Path.__parse(s, isSplit = isSplit)

        if not cpath:
            raise ValueError("Given string does not represent a CPath. ")

        return cpath

    def __add__(self, other):
        """ Adds a path to the end of this path.

        :param other: Path to add.
        :type other: Any

        :rtype: Path
        """

        return Path.parse("%s%s" % (ustr(self), ustr(other)))

    def __mod__(self, other):
        """ Adds a new component with a "?" to the end of this Path.

        :param other: Other path to add.
        :type other: Any

        :rtype: Path
        """

        return self + ('?' + ustr(other))

    def __div__(self, other):
        """ Adds a new component with a "/" to the end of this Path.

        :param other: Other path to add.
        :type other: Any

        :rtype: Path
        """

        return self + ('/' + ustr(other))

    def __truediv__(self, other):
        """ Same as __div__(self, other).

        :param other: Other path to add.
        :type other: Any

        :rtype: Path
        """

        return self.__div__(other)

    def __getitem__(self, key):
        """ Same as __mod__(self, key).

        :param key: Other path to add.
        :type key: Any

        :rtype: Path
        """

        return self % key

    def __getattr__(self, key):
        """ Same as __getitem__, but might not work for all paths.

        :param key: Other path to add.
        :type key: Any

        :rtype: Path
        """

        return self[key]

class LNStep(AbstractCaseClass):
    """ Represents a step in a LocalName instance. """

    @staticmethod
    def parse(s):
        """ Parses a string into an LNStep.

        :param s: String to prase
        :type s: str
        :rtype: LNStep
        """

        s = ustr(s)
        if s.startswith("[") and s.endswith("]"):
            return ComplexStep(Path.parseM(s[1:-1]))
        else:
            return SimpleStep(s)


class SimpleStep(LNStep):
    """ Represents a simple LNStep. """

    def __init__(self, name):
        """ Creates a new LNStep instance.

        :parm name: Name of the LNStep.
        :type name: str
        """

        super(SimpleStep, self).__init__()

        self.__name = name  # type: str

    @property
    def name(self):
        """ Returns the name of this LNStep.

        :rtype: str
        """

        return self.__name

    def __str__(self):
        """ Turns this SimpleStep instance into a string.

        :rtype: str
        """

        return self.name


class LocalName(CaseClass):
    """ Represents a LocalName of an object in MMT. """

    def __init__(self, steps):
        """ Creates a new LocalName.

        :param steps: List of LNSteps this LocalName consists of.
        :type steps: list
        """

        self.__steps = steps

    @property
    def steps(self):
        """ Returns a list of LNSteps used by this LocalName.

        :rtype: list
        """

        return self.__steps

    def __str__(self):
        """ Turns this LocaName into a string.

        :rtype: str
        """

        return "/".join(map(ustr, self.steps))

    @staticmethod
    def split(s):
        """ Splits a string into multiple strings to be as LNStep instances.

        :param s: String to split.
        :type s: str

        :rtype: list
        """

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
        """ Parses a string into a LocalName.

        :param s: String to split.
        :type s: str

        :rtype: LocalName
        """

        # split into segments
        segments = LocalName.split(s)

        # and parse those individually
        return LocalName(list(map(lambda s: LNStep.parse(s), segments)))


class DPath(Path):
    """ Represents a path to a document. """

    def __init__(self, u):
        """ Creates a new DPath instance.

        :param u: URI of document to reference.
        :type u: URI
        """

        super(DPath, self).__init__()

        self.__uri = u  # type: uri.URI

    @property
    def uri(self):
        """ Returns the URI of the document this path references.

        :rtype: uri.URI
        """

        return self.__uri

    def __str__(self):
        """ Turns this DPath into a string.

        :rtype: str
        """

        return "%s" % (ustr(self.uri), )


class ContentPath(Path, AbstractCaseClass):
    """ Represents the path to any type of content inside MMT. """

    def __init__(self, module):
        """ Creates a new ContentPath() instance.

        :param module: Parent Module of this Content Path.
        :type module: MPath
        """

        self.__module = module  # type: MPath

    @property
    def module(self):
        """ Returns the module of this ContentPath.

        :rtype: MPath
        """

        return self.__module


    def toTerm(self):
        """ Turns this ContentPath into a term by wrapping it in an OMID.

        :rtype omid.OMID
        """

        from MMTPy.content.objects.terms import omid
        return omid.OMID(self)

    def __call__(self, *args, **kwargs):
        """ Equivalent to self.toTerm().call. """

        return self.toTerm().__call__(*args, **kwargs)

    def __invert__(self):
        """ Same as self.toTerm().

        :rtype: omid.OMID
        """

        return self.toTerm()


class CPath(Path):
    """ Represents a path to a component. """

    def __init__(self, parent, component):
        """ Creates a new CPath instance.

        :param parent: Parent declaration to point to.
        :type parent: ContentPath

        :param component: Name of component to point.
        :type component: str
        """

        super(CPath, self).__init__()

        self.__parent = parent  # type: ContentPath
        self.__component = component  # type: str

    @property
    def parent(self):
        """ Returns the parent path of this CPath.

        :rtype: ContentPath
        """

        return self.__parent

    @property
    def component(self):
        """ Returns the component of this CPath.

        :rtype: str
        """

        return self.__component

    def __str__(self):
        """ Turns this CPath into a string.

        :rtype: str
        """

        return "%s?%s" % (self.parent, self.component)


class MPath(ContentPath):
    """ Represents a path to a module. """

    def __init__(self, parent, name):
        """ Creates a new MPath instance.

        :param parent: Path to parent Namespace.
        :type parent: DPath

        :param name: Name of this Module.
        :type name: LocalName
        """

        super(MPath, self).__init__(self)

        self.__parent = parent  # type: DPath
        self.__name = name  # type: LocalName

    @property
    def parent(self):
        """ Returns the parent of this MPath.

        :rtype: DPath
        """

        return self.__parent

    @property
    def name(self):
        """ Returns the name of this MPath.

        :rtype: LocalName
        """

        return self.__name

    def __str__(self):
        """ Turns this MPath into a string.

        :rtype: str
        """

        return "%s?%s" % (self.parent, self.name)


class GlobalName(ContentPath):
    """ Represents the Path to a single Symbol. """

    def __init__(self, module, name):
        """ Creates a new GlobalName() instance.

        :param module: Module this Symbol is located in.
        :type module: MPath

        :param name: Name of the symbol.
        :type name: LocalName
        """

        super(GlobalName, self).__init__(module)

        self.__name = name  # type: LocalName

    @property
    def name(self):
        """ Returns the name of this Symbol.

        :rtype: LocalName
        """

        return self.__name

    def __str__(self):
        """ Turns this GlobalName into a string.

        :rtype: str
        """

        return "%s?%s" % (self.module, self.name)


class ComplexStep(LNStep):
    """ Represents a complex LNStep. """

    def __init__(self, path):
        """ Creates a new ComplexStep() instance.

        :param path: Path that is wrapped by this ComplexStep instance.
        :type path: MPath
        """
        super(ComplexStep, self).__init__()

        self.__path = path  # type: MPath

    @property
    def path(self):
        """ Returns the Path wrapped by this ComplexStep() instance.

        :rtype: MPath
        """

        return self.__path

    def __str__(self):
        """ Turns this ComplexStep into a string.

        :rtype: str
        """

        return "[%s]" % (self.path, )


__all__ = ["LNStep", "SimpleStep", "Path", "LocalName", "Path", "DPath",
           "ContentPath", "CPath", "MPath", "GlobalName", "ComplexStep"]