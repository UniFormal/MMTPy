# Load any etree implementation. 
# adapted from http://lxml.de/tutorial.html
try:
  from lxml import etree
  etree_implementation = "lxml.etree"
except ImportError:
  try:
    # Python 2.5
    import xml.etree.cElementTree as etree
    etree_implementation = "cElementTree (Python 2.5+)"
  except ImportError:
    try:
      # Python 2.5
      import xml.etree.ElementTree as etree
      etree_implementation = "ElementTree (Python 2.6+)"
    except ImportError:
      try:
        # normal cElementTree install
        import cElementTree as etree
        etree_implementation = "cElementTree"
      except ImportError:
        try:
          # normal ElementTree install
          import elementtree.ElementTree as etree
          etree_implementation = "ElementTree"
        except ImportError:
          print("Unable to import any known ElementTree implementation. Please install lxml or a similar module. Some functionality might not work. ")
# Load requests
try:
    import requests
except ImportError:
    print("Unablem to import the requests module. Some functionality might not work. ")