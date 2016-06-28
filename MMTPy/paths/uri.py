"""
This file defines URIs for MMT.
"""

from case_class import CaseClass

import re

uri_expr = re.compile(
    r"^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?"
)


class URI(CaseClass):
    """ An object version of a URI. """

    def __init__(self, scheme, authority, path=None, absolute=False,
                 query=None, fragment=None):
        """ Creates a new URI instance.

        :param scheme: Scheme used by the URI. Commonly one of 'http', 'https'.
        :type scheme: str

        :param authority: Authority part of the URI.
        :type authority: str

        :param path: Path components of the URI seperated by '/'s.
        :type path: list

        :param absolute: Is this an absolute URI?
        :type absolute: bool

        :param query: Query part of the URL
        :type query: str

        :param fragment: Frament part of the URI
        :param fragment: str
        """

        self.__absolute = absolute  # type: bool

        self.__scheme = scheme  # type: str

        self.__authority = authority  # type: str

        self.__path = path if path is not None else []  # type: str

        self.__query = query  # type: str

        self.__fragment = fragment  # type: str

    @property
    def absolute(self):
        """ Returns if this URI is absolute.

        :rtype: bool
        """

        return self.__absolute

    @property
    def scheme(self):
        """ Returns the scheme of this URI.

        :rtype: str
        """

        return self.__scheme

    @property
    def authority(self):
        """ Returns the authority of this URI.

        :rtype: str"""

        return self.__authority

    @property
    def path(self):
        """ Returns a list of strings representing the path components
        of this URI.

        :rtype: list
        """

        return self.__path

    @property
    def query(self):
        """ Returns the query used by this URI.

        :rtype: str"""

        return self.__query

    @property
    def fragment(self):
        """ Returns the fragment used by this URI.

        :rtype: str"""

        return self.__fragment

    def __str__(self):
        """ Turns this URI into a string.

        :rtype: str"""

        uri_str = ""

        if self.scheme:
            uri_str += self.scheme + ":"

        if self.authority:
            uri_str += "//" + self.authority

        uri_str += ("/" if self.absolute else "") + "/".join(self.path)

        if self.query:
            uri_str += "?" + self.query

        if self.fragment:
            uri_str += "#" + self.fragment

        return uri_str

    def __repr__(self):
        """ Turns this URI into a string representation.

        :rtype: str"""

        return "URI(%r)" % (str(self), )

    @staticmethod
    def parse(uri):
        """ Parses a string into a URI.

        :param uri: String to parse.
        :type uri: str
        """

        m = uri_expr.match(uri)
        if not m:
            raise ValueError("%s is not a malformed URI")

        # extract scheme and authority
        scheme = m.group(2) if m.group(2) is not None else ""
        authority = m.group(4) if m.group(4) is not None else ""

        # find the requested path
        jpath = m.group(5) if m.group(5) is not None else ""

        # and check if it is absolute
        (pathString, absolute) = (jpath[1:], True) if jpath.startswith(
            "/") else (jpath, False)

        # split the path components
        path = pathString.split("/")
        if path == [""]:
            path = []

        # extract query and fragment
        query = m.group(7) if m.group(7) is not None else ""
        fragment = m.group(9) if m.group(9) is not None else ""

        return URI(scheme, authority, path, absolute, query, fragment)

__all__ = ["URI"]