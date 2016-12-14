"""
Defines the Torrent class used to store parsed data from a metainfo file.
"""


class Torrent:
    """
    The class for the metainfo (torrent) file.
    """

    info = None
    announce = None
    announce_list = None
    creation_date = None
    comment = None
    created_by = None
    encoding = None

    class Info:
        """
        The attributes for the "info" field.
        """
        piece_length = None
        pieces = None
        private = None
        name = None
        length = None
        checksum = None
        checksum_type = None
        files = []

    class File:
        """
        The class for the "files" field.
        """
        length = None
        checksum = None
        checksum_type = None
        path = None

    class Error(Exception):
        """
        The class for exceptions raised as a result of interacting with TorrentFiles.
        """
        pass