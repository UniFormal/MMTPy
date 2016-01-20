from . import types

def matches(o, pattern):
    """
    Checks if an object o matches a pattern.

    Returns a pair of (matches, )
    """

    from . import caseclass

    # for a case class, use the appropriate method
    if isinstance(pattern, caseclass.StaticCaseClass):
        return pattern.__matches__(o)

    # VALUE matching
    if o == pattern:
        return True

    # instance checking
    if isinstance(pattern, types.typetype):
        return isinstance(o, pattern)

    # if the pattern is MatchEverything(), we always match
    return pattern == MatchEverything()

from . import caseclass
class MatchEverything(caseclass.make()):
    def __init__(self):
        super(MatchEverything, self).__init__()
