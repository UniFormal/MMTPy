import unittest
from MMTPy.paths.uri import URI

class TestURI(unittest.TestCase):

    URIS = {
        '/': URI('', '', [], True, '', ''),
        '': URI('', '', [], False, '', ''),

        'http://authority/path/segments?query#fragment':
            URI('http', 'authority', ['path', 'segments'], True, 'query',
                'fragment'),
        'path/segments?query#fragment':
            URI('', '', ['path', 'segments'], False,
                'query', 'fragment'),
    }

    def test_parse(self):
        """ Test if URIs can be parsed properly. """

        for k in TestURI.URIS:
            self.assertEqual(URI.parse(k), TestURI.URIS[k], 'parsing a URI')

    def test___str__(self):
        """ Test if the stringification of URIs works as exepected. """

        for k in TestURI.URIS:
            self.assertEqual(str(TestURI.URIS[k]), k, 'stringifying a URI')