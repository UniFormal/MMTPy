import unittest
from MMTPy.content.componentkey import *


class TestComponentKey(unittest.TestCase):
    examples = {
        "type": TypeComponent(),
        "definition": DefComponent(),
        "domain": DomComponent(),
        "codomain": CodComponent(),
        "params": ParamsComponent(),
        "pattern-body": PatternBodyComponent(),
        "metadata": MetaDataComponent(),
        "ext-example": OtherComponent("example")
    }

    def test___str__(self):
        """ Tests if we can str() ComponentKey() properly"""

        for k in TestComponentKey.examples:
            self.assertEqual(str(TestComponentKey.examples[k]), k,
                             "str() a ComponentKey")