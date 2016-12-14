"""
Contains the unit tests to test the torrent.py classes.
"""

import unittest
from torrentparser.torrent import Torrent


class TestTorrentFile(unittest.TestCase):

    def test_torrent_file_has_attributes(self):
        self.assertIsNone(Torrent.info)
        self.assertIsNone(Torrent.announce_list)
        self.assertIsNone(Torrent.announce)
        self.assertIsNone(Torrent.creation_date)
        self.assertIsNone(Torrent.comment)
        self.assertIsNone(Torrent.created_by)
        self.assertIsNone(Torrent.encoding)

    def test_torrent_file_info_has_attributes(self):
        self.assertListEqual(Torrent.Info.files, [])
        self.assertIsNone(Torrent.Info.length)
        self.assertIsNone(Torrent.Info.md5sum)
        self.assertIsNone(Torrent.Info.name)
        self.assertIsNone(Torrent.Info.pieces)
        self.assertIsNone(Torrent.Info.piece_length)

    def test_torrent_file_file_has_attributes(self):
        self.assertIsNone(Torrent.File.md5sum)
        self.assertIsNone(Torrent.File.length)
        self.assertIsNone(Torrent.File.path)
