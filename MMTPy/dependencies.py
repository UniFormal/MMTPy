# TODO: Delete this file once no longer needed

from lxml import etree
etree_type = etree._Element
del etree

__all__ = ["etree_type"]