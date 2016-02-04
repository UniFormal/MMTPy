from MMTPy.clsutils import types, caseclass
from MMTPy.dependencies import etree, etree_type

from MMTPy.utils import ustr

from copy import deepcopy

def match_tag(node, pattern):
    """
    Matches a node against a string pattern.

    In case of an empty pattern, any tag is matched.
    In case of a namespace pattern, any tag of that namespace is matched.
    """

    # if we have an empty tagname
    if pattern == "":
        return True

    # if we have a namespace
    if pattern.startswith("{") and pattern.endswith("}"):
        return node.tag.startswith(pattern)

    # all other cases
    return node.tag == pattern

def match(node, pattern):
    """
    Matches a node against a pattern. Returns a pair of (matching, nodes) where
    matching is a boolean that indicates if the pattern matches and nodes a tuple
    of nodes corresponding to the structure of the matched nodes.

    A pattern must be one of the following two:

        1) A single node matches (see match_tag)
        2) A pair of (tag, children) where tag is a single node match (see
            match_single_tag) and children is a tag list (see match_tag_list)
    """

    # matching a single pattern
    if isinstance(pattern, types.strtype):
        if match_tag(node, pattern):
            return True, node
        else:
            return False, None

    # matching a tag, children combo
    (tag, children) = pattern

    # if we match the single tag, we need to now look at the children
    if match_tag(node, tag):
        (csuc, cmatch) = match_tag_list(list(node), children)

        if csuc:
            return True, (node, cmatch)
        else:
            return False, __empty_match__(pattern)
    else:
        return False, __empty_match__(pattern)

def matches(node, pattern):
    """
    Same as match(node, pattern) except that it only returns a boolean
    indicating if the node is matched.
    """
    (matches, _) = match(node, pattern)
    return matches


def match_tag_list(nodes, patterns):
    """
    Matches a list of nodes against a tag list.

    A tag list must be one of the following:

        1) None. Any list of nodes is matched.
        2) An array of pattern (see match)
    """

    # if nothing is to be matched, we are done
    if patterns == None:
        return True, nodes

    matches = []

    # else we have a list of matches to check
    for n, p in zip(nodes, patterns):

        # check them individually
        (es, em) = match(n, p)

        if not es:
            return False, __empty_match_list__(patterns)

        matches.append(em)

    # and return the matches as a tuple
    return True, tuple(matches)

def __empty_match__(pattern):
    """
    Returns an empty match for the tag pattern.
    """

    # matching a single pattern
    if isinstance(pattern, types.strtype):
        return None

    # matching a composite pattern
    (tag, children) = pattern

    # return the empty match list
    return (None, __empty_match_list__(children))

def __empty_match_list__(patterns):

    """
    Returns an empty match list for the tag list patterns.
    """

    if patterns == None:
        return None

    return tuple(list(map(__empty_match__, patterns)))

def make_element(tag, *children, **attributes):
    """
        Makes a new XML Element

        tag -- The name of the tag to create
        children -- A list of children to create. Each child should be of one of
            the following forms:

            1. tag
            2. (tag,)
            3. (tag, children)
            4. (tag, children, attributes)
        attributes -- List of attributes to create. Use the empty attribute for text content
    """

    # Create the element first.

    # if it is already an element
    if isinstance(tag, etree_type):
        me = tag
    # if it is a tuple, it should be (tag_name, text)
    elif isinstance(tag, tuple):
        me = etree.Element(tag[0])
        me.text = str(tag[1])
    # else it is just a tag name
    else:
        me = etree.Element(tag)

    # set the attributes
    for (a, v) in attributes.items():
        if a == "":
            me.text = ustr(v)
        else:
            me.set(a, ustr(v))

    # now iterate through the children
    for c in children:

        # take all the different cases into account
        if isinstance(c, tuple):
            if len(c) == 1:
                (ct,) = c
                (cc, ca) = ([], {})
            elif len(c) == 2:
                (ct,cc) = c
                ca = {}
            else:
                (ct,cc,ca) = c
        else:
            ct = c
            (cc, ca) = ([], {})

        # and add a proper child element
        me.append(make_element(c, *cc, **ca))

    # finally return the generated element
    return me

def copy(node):
    """
    Returns a deep copy of an xml node.
    """

    return deepcopy(node)

def textcontent(node):
    """
    Gets text content of a node
    """

    pretext =  "" if node.text == None else node.text
    posttext = "" if node.tail == None else node.tail

    return pretext + "\n".join(node.itertext()) + posttext


openmath_ns = "http://www.openmath.org/OpenMath"

def omt(tag = ""):
    """
    Wraps a tag name in the OpenMath Namespace
    """
    return "{"+openmath_ns+"}"+tag

etree.register_namespace("om", openmath_ns)
