import unittest
import arkpy


class TestArkpy(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_length(self):
        ark = arkpy.mint(authority='66666', template='eeddk')
        # 11 = 5 (from '66666' authority)
        #    + 1 (from '/')
        #    + 5 (from 'eedd' template)
        self.assertEqual(len(ark), 11)

    def test_bare(self):
        ark = arkpy.mint(authority='66666', template='eeddk')
        ark2 = arkpy.mint(authority='66666', template='dedededk', bare=False)
        self.assertFalse(ark.startswith('ark:/'))
        self.assertTrue(ark2.startswith('ark:/'))

    def test_authority_required(self):
        self.assertRaises(TypeError, arkpy.mint)
        self.assertRaises(TypeError, arkpy.mint, template='eeddk')

    def test_template_required(self):
        self.assertRaises(TypeError, arkpy.mint)
        self.assertRaises(TypeError, arkpy.mint, authority='66666')

    def test_prefix(self):
        ark = arkpy.mint(authority='66666', template='eeddk', prefix='dc')
        parts = ark.split('/')
        identifier = parts[1]
        self.assertTrue(identifier.startswith('dc'))

    def test_template_digits(self):
        ark = arkpy.mint(authority='66666', template='ddddddddd')
        parts = ark.split('/')
        identifier = parts[1]
        for char in identifier:
            self.assertTrue(char in arkpy.digits)

    def test_template_xdigits(self):
        ark = arkpy.mint(authority='66666', template='eeeeeeeee')
        parts = ark.split('/')
        identifier = parts[1]
        for char in identifier:
            self.assertTrue(char in arkpy.xdigits)

    def test_validate_known_valid(self):
        ark = '13030/f54x54g11'
        self.assertTrue(arkpy.validate(ark))

    def test_validate_known_invalid(self):
        ark = '13030/f54x54g10'
        self.assertFalse(arkpy.validate(ark))

    def test_validate_known_valid_with_scheme(self):
        ark = 'ark:/13030/f54x54g11'
        self.assertTrue(arkpy.validate(ark))

    def test_validate_known_invalid_with_scheme(self):
        ark = 'ark:/13030/f54x54g10'
        self.assertFalse(arkpy.validate(ark))

    def test_validate_bare_and_nonbare(self):
        ark = arkpy.mint(authority='66666', template='ddeeddeek', bare=False)
        ark2 = arkpy.mint(authority='66666', template='ddeeddeek', bare=True)
        self.assertTrue(arkpy.validate(ark))
        self.assertTrue(arkpy.validate(ark2))

if __name__ == '__main__':
    unittest.main()
