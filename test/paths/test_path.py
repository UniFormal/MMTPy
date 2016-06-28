import unittest

from MMTPy.paths.path import LNStep, SimpleStep, ComplexStep, DPath, MPath, \
    LocalName, Path, GlobalName, CPath
from MMTPy.content.componentkey import DefComponent
from MMTPy.paths.uri import URI


class TestPath(unittest.TestCase):
    def test_split(self):
        """ Tests if we can split a path properly. """

        self.assertEqual(
            Path.split('http://document?module?symbol?component'),
            ('http://document', 'module', 'symbol', 'component'),
            'splitting a path with SimpleSteps'
        )

        self.assertEqual(
            Path.split('http://document?[a_b]?[c_d]?[e_f]'),
            ('http://document', '[a_b]', '[c_d]', '[e_f]'),
            'splitting a path with ComplexSteps'
        )

    def test_parseD(self):
        """ Tests if we can parse a document path properly. """

        self.assertEqual(Path.parseD('http://the/document'),
                         DPath(URI.parse('http://the/document')))

    def test_parseM(self):
        """ Tests if we can parse a module path properly. """

        self.assertEqual(Path.parseM('http://document?module'),
                         MPath(DPath(URI.parse('http://document')),
                               LocalName([SimpleStep('module')])))

    def test_parseS(self):
        """ Test if we can parse GlobalName properly. """

        self.assertEqual(Path.parseS('http://document?module?symbol'),
            GlobalName(MPath(DPath(URI.parse('http://document')),
                               LocalName([SimpleStep('module')])),
                       LocalName([SimpleStep('symbol')])))

    def test_parseC(self):
        """ Test if we can parse a content path properly. """

        self.assertEqual(
            Path.parseC('http://document?module?symbol?definition'),
                     CPath(GlobalName(MPath(DPath(URI.parse('http://document')),
                           LocalName([SimpleStep('module')])),
                   LocalName([SimpleStep('symbol')])), DefComponent()))




class TestLNStep(unittest.TestCase):
    examples = {
        'simple': SimpleStep('simple'),
        '[ns?module]':
            ComplexStep(MPath(DPath(URI.parse('ns')), LocalName(
                [SimpleStep('module')])))
    }

    def test_parse(self):
        """ Test if LNSteps can be parsed properly. """

        for k in TestLNStep.examples:
            self.assertEqual(LNStep.parse(k), TestLNStep.examples[k],
                             'parsing an LNStep')

    def test___str__(self):
        """ Test if the str() of LNSteps works as exepected. """

        for k in TestLNStep.examples:
            self.assertEqual(str(TestLNStep.examples[k]), k, 'stringifying an LNStep')


class TestLocalName(unittest.TestCase):
    examples = {
        'simple/simple': LocalName([SimpleStep('simple'),
                                    SimpleStep('simple')]),
        '[ns?module]/simple': LocalName([ComplexStep(MPath(
            DPath(URI.parse('ns')), LocalName([SimpleStep('module')]))),
            SimpleStep('simple')])
    }

    def test_parse(self):
        """ Test if LocaNames can be parsed properly. """

        for k in TestLocalName.examples:
            self.assertEqual(LocalName.parse(k), TestLocalName.examples[k],
                             'parsing a LocalName')

    def test___str__(self):
        """ Test if the str() of LocalSteps works as exepected. """

        for k in TestLocalName.examples:
            self.assertEqual(str(TestLocalName.examples[k]), k,
                             'stringifying a LocalName')


class TestDPath(unittest.TestCase):
    examples = {
        "http://example": DPath(URI.parse('http://example'))
    }

    def test___str__(self):
        """ Test if DPath str() works as expected. """
        for k in TestDPath.examples:
            self.assertEqual(str(TestDPath.examples[k]), k,
                             'str() a DPath. ')


class TestCPath(unittest.TestCase):
    examples = {
        'http://document?module?symbol?definition': CPath(GlobalName(MPath(
            DPath(URI.parse('http://document')),
            LocalName([SimpleStep('module')])),
            LocalName([SimpleStep('symbol')])), DefComponent())
    }

    def test___str__(self):
        """ Test if CPath str() works as expected. """

        for k in TestCPath.examples:
            print(str(TestCPath.examples[k]))
            self.assertEqual(str(TestCPath.examples[k]), k,
                             'str() a CPath. ')


class TestMPath(unittest.TestCase):
    examples = {
        'http://document?module': MPath(DPath(URI.parse('http://document')),
                                        LocalName([SimpleStep('module')]))
    }

    def test___str__(self):
        """ Test if MPath str() works as expected. """

        for k in TestMPath.examples:
            self.assertEqual(str(TestMPath.examples[k]), k,
                             'stringifying an MPath. ')


class TestGlobalName(unittest.TestCase):
    examples = {
        'http://document?module?symbol': GlobalName(MPath(DPath(
            URI.parse('http://document')), LocalName([SimpleStep('module')])),
            LocalName([SimpleStep('symbol')]))
    }

    def test___str__(self):
        """ Test if GlobalName str() works as expected. """

        for k in TestGlobalName.examples:
            self.assertEqual(str(TestGlobalName.examples[k]), k,
                             'str() a GlobalName. ')


class TestComplexStep(unittest.TestCase):
    examples = {
        '[http://document?module]': ComplexStep(MPath(DPath(
            URI.parse('http://document')), LocalName([SimpleStep('module')])))
    }

    def test___str__(self):
        """ Test if ComplexStep str() works as expected. """

        for k in TestComplexStep.examples:
            self.assertEqual(str(TestComplexStep.examples[k]), k,
                             'str() a ComplexStep. ')

