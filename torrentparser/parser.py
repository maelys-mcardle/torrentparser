"""
Provides the functions to parse a .torrentfile.
"""

from .bencoding import decode_dictionary, BencodingDecodeException
from .torrent import Torrent
import datetime


def parse_torrent_file(file_path):
    """
    Loads the torrent file, returning a TorrentFile of its contents.
    :param file_path:
    :return:
    """

    # Parse the torrent file as a dictionary.
    # The contents are known as metainfo.
    metainfo = parse_torrent_file_as_dictionary(file_path)

    # Dictionary could not be loaded. Raise exception.
    if not metainfo:
        raise Torrent.Error("Could not parse torrent file")

    # Instantiate a new TorrentFile object.
    torrent = Torrent

    # Populate TorrentFile object.
    if "announce" in metainfo:
        torrent.announce = metainfo["announce"]

    if "announce-list" in metainfo:
        torrent.announce_list = metainfo["announce-list"]

    if "creation date" in metainfo:
        unix_time = metainfo["creation date"]
        torrent.creation_date = datetime.datetime.fromtimestamp(unix_time)

    if "comment" in metainfo:
        torrent.comment = metainfo["comment"]

    if "encoding" in metainfo:
        torrent.encoding = metainfo["encoding"]

    if "info" in metainfo:
        torrent.info = Torrent.Info()
        metainfo_info = metainfo["info"]

        if "piece length" in metainfo_info:
            torrent.info.piece_length = metainfo_info["piece length"]

        if "pieces" in metainfo_info:
            torrent.info.pieces = metainfo_info["pieces"]

        if "private" in metainfo_info:
            torrent.info.private = metainfo_info["private"]

        if "name" in metainfo_info:
            torrent.info.name = metainfo_info["name"]

        if "length" in metainfo_info:
            torrent.info.length = metainfo_info["length"]

        if "md5sum" in metainfo_info:
            torrent.info.checksum = metainfo_info["md5sum"]
            torrent.info.checksum_type = "MD5"

        if "md5" in metainfo_info:
            torrent.info.checksum = metainfo_info["md5"]
            torrent.info.checksum_type = "MD5"

        if "sha1" in metainfo_info:
            torrent.info.checksum = metainfo_info["sha1"]
            torrent.info.checksum_type = "SHA1"

        if "files" in metainfo_info:
            torrent_files = []
            for single_file in metainfo_info["files"]:
                torrent_file = Torrent.File()

                if "length" in single_file:
                    torrent_file.length = single_file["length"]

                if "md5sum" in single_file:
                    torrent_file.checksum = single_file["md5sum"]
                    torrent_file.checksum_type = "MD5"

                if "md5" in single_file:
                    torrent_file.checksum = single_file["md5"]
                    torrent_file.checksum_type = "MD5"

                if "sha1" in single_file:
                    torrent_file.checksum = single_file["sha1"]
                    torrent_file.checksum_type = "SHA1"

                if "path" in single_file:
                    torrent_file.path = single_file["path"]

                torrent_files.append(torrent_file)

            torrent.info.files = torrent_files

    return torrent


def parse_torrent_file_as_dictionary(file_path):
    """
    Loads the torrent file, returning a dictionary of its contents.
    :param file_path: The path to the metainfo (torrent) file.
    :return: The decoded file contents, as a dictionary.
    """

    # Open the issued file path.
    with open(file_path) as torrent_file:

        # Try decoding the contents of the file.
        # Return them if decoded succesfully.
        try:
            dictionary, size = decode_dictionary(torrent_file.read())
            return dictionary

        # If the file could not be decoded, return a None object.
        except BencodingDecodeException:
            return None


