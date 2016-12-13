import unittest
from torrentparser.bencoding import decode_byte_string


class TestBencodingByteString(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(decode_byte_string("13:hello, world!"), ('hello, world!', 16))

    def test_multiple_colons(self):
        self.assertEqual(decode_byte_string("5:hi: !"), ('hi: !', 7))

    def test_zero_length(self):
        self.assertEqual(decode_byte_string("0:"), ('', 2))

