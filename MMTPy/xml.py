from lxml import etree

from . import utils

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
        Matches a node against a pattern. 
        
        A pattern must be one of the following two:
        
            1) A single node matches (see match_tag)
            2) A pair of (tag, children) where tag is a single node match 
                (see match_single_tag) and children is a tag list 
                (see match_tag_list) 
    """
    
    # matching a single pattern
    if isinstance(pattern, utils.stringcls):
        if match_tag(node, pattern):
            return True, node
        else:
            return False, None
    
    # matching a tag, children combo
    (tag, children) = pattern
    
    # if we match the single tag
    if match_tag(node, tag):
        (csuc, cmatch) = match_tag_list(list(node), children)
        
        if csuc:
            return True, (node, cmatch)
        else:
            return False, empty_match(pattern)
    else:
        return False, empty_match(pattern)
    
    
def match_tag_list(nodes, patterns):
    """
        Matches a list of nodes against a tag list. 
        
        A tag list must be one of the following: 
        
            1) None. Any list of nodes is matched. 
            2) An array of pattern (see match)
    """
    
    if patterns == None:
        return True, nodes
    
    matches = []
    
    for n, p in zip(nodes, patterns):
        
        (es, em) = match(n, p)
        
        if not es:
            return False, empty_match_list(patterns)
        
        matches.append(em)
    
    return True, tuple(matches)

def empty_match(pattern):
    """
        Returns an empty match for the tag pattern. 
    """
    
    # matching a single pattern
    if isinstance(pattern, utils.stringcls):
        return None
    
    # matching a composite pattern
    (tag, children) = pattern
    
    # return the empty match list
    return (None, empty_match_list(children))
    
def empty_match_list(patterns):
    
    """
        Returns an empty match list for the tag list patterns. 
    """
    
    if patterns == None:
        return None
    
    return tuple(list(map(empty_match, patterns)))
    
def make_element(tag, *children, **attributes):
    """
        Makes a new XML Element
    """
    me = etree.Element(tag)
    
    for (a, v) in attributes.items():
        me.set(a, v)
    
    for c in children:
        me.append(make_element(c))
    
    return me

# Namespace for openmath
omn = "http://www.openmath.org/OpenMath"
def omt(tag = ""):
    return "{"+omn+"}"+tag
