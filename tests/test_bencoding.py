import unittest
from torrentparser.bencoding import decode_byte_string, decode_integer, decode_list, decode_dictionary, \
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

    def test_simple_list(self):
        self.assertEqual(decode_list("l4:spam4:eggse"), (["spam", "eggs"], 14))

    def test_list_with_integer(self):
        self.assertEqual(decode_list("l4:spami3ee"), (["spam", 3], 11))


class TestBencodingDictionary(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(decode_dictionary("de"), ({}, 2))

    def test_simple_dict(self):
        self.assertEqual(decode_dictionary("d3:cow3:moo4:spam4:eggse"),
                         ({
                             "cow": "moo",
                             "spam": "eggs"
                         }, 24))

    def test_longer_dict(self):
        self.assertEqual(decode_dictionary(
            "d9:publisher3:bob17:publisher-webpage15:www.example.com" +
            "18:publisher.location4:homee"),
            ({
                "publisher": "bob",
                "publisher-webpage": "www.example.com",
                "publisher.location": "home"
            }, 83))
