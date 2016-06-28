import unittest
from MMTPy.content.position import Position


class TestPosition(unittest.TestCase):
    examples = {
        "1_2_3_4": Position([1, 2, 3, 4]),
        "": Position([])
    }

    def test___str__(self):
        """ Tests if we can str() a Position() properly"""

        for k in TestPosition.examples:
            self.assertEqual(str(TestPosition.examples[k]), k,
                             "str() a Position")

    def test_parse(self):
        """ Tests if we can parse a Position() properly"""

        for k in TestPosition.examples:
            self.assertEqual(Position.parse(k), TestPosition.examples[k],
                             "parse a Position")