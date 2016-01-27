def ustr(s):
    """
    Returns a string version of s.
    When available uses unicode(), else str()
    """
    try:
        return unicode(s)
    except NameError:
        return str(s)
