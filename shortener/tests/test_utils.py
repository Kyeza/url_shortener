import unittest

from shortener.utils import shortener_base62_encoder as encoder


class UtilsTestCase(unittest.TestCase):

    def test_shortener_base62_encoder(self):
        num = 1
        expected = 'b'

        self.assertEqual(encoder(num), expected, msg=f'Expected: {expected} | Result: {encoder(num)}')
