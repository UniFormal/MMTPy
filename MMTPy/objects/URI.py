import re
from MMTPy.caseclass import caseclass
from MMTPy.caseclass import types

uriexpr = re.compile(r"^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?")

class URI(caseclass.make((types.strtype,), (types.strtype,), [types.strtype], bool, (types.strtype,), (types.strtype,))):
    """
    An object version of a URI
    """

    def __init__(self, scheme, authority, path = [], absolute = False, query = None, fragment = None):
        super(URI, self).__init__(scheme, authority, path, absolute, query, fragment)

        self.absolute = absolute
        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment

    def __str__(self):
        uristr = ""

        if self.scheme:
            uristr += self.scheme + ":"

        if self.authority:
            uristr += "//" + self.authority

        uristr += ("/" if self.absolute else "") + "/".join(self.path)

        if self.query:
            uristr += "?" + self.query

        if self.fragment:
            uristr += "#" + self.fragment

        return uristr
    def __repr__(self):
        return "URI(%r)" % str(self)

    @staticmethod
    def parse(uri):
        """
        Parses a string into a URI obj.Obj
        """
        m = uriexpr.match(uri)
        if not m:
            raise ValueError("%s is not a malformed URI")

        # extract scheme and authority
        scheme = m.group(2)
        authority = m.group(4)

        # find the requested path
        jpath = m.group(5)

        # and check if it is absolute
        (pathString, absolute) = (jpath[1:], True) if jpath.startswith("/") else (jpath, False)

        # split the path components
        path = pathString.split("/")
        if path == [""]:
            path = []

        # extract query and fragment
        query = m.group(7)
        fragment = m.group(9)

        return URI(scheme, authority, path, absolute, query, fragment)
