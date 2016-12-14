import unittest
from torrentparser.bencoding import decode_byte_string, decode_integer, decode_list, decode_dictionary,\
    BencodingDecodeException


class TestBencodingByteString(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(decode_byte_string("13:hello, world!"), ('hello, world!', 16))

    def test_multiple_colons(self):
        self.assertEqual(decode_byte_string("5:hi: !"), ('hi: !', 7))

    def test_zero_length(self):
        self.assertEqual(decode_byte_string("0:"), ('', 2))


class TestBencodingInteger(unittest.TestCase):

    def test_empty(self):
        with self.assertRaises(BencodingDecodeException):
            decode_integer("ie")

    def test_zero(self):
        self.assertEqual(decode_integer("i0e"), (0, 3))

    def test_positive(self):
        self.assertEqual(decode_integer("i365e"), (365, 5))

    def test_negative(self):
        self.assertEqual(decode_integer("i-65e"), (-65, 5))

    def test_64bit(self):
        self.assertEqual(decode_integer("i18446744073709551615e"), (18446744073709551615, 22))


class TestBencodingList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(decode_list("le"), ([], 2))
