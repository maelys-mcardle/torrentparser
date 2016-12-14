"""
Provides a command-line interface to show the contents of torrent files.
"""
import argparse
from .parser import parse_torrent_file
from .torrent import Torrent


def main():
    """
    The entry point for the invocation of the command-line.
    :return: None.
    """

    # Parse the command-line arguments.
    torrent_file_path, is_verbose = parse_command_line()

    # Load the torrent file.
    try:
        torrent = parse_torrent_file(torrent_file_path)

    # Could not open the torrent file.
    except IOError as io_error:
        print(io_error.strerror)

    # Could not parse the torrent file. Show the reason.
    except Torrent.Error as torrent_error:
        print(torrent_error)

    # Parsed the torrent file.
    else:
        print_torrent_file_contents(torrent, is_verbose)

    return None


def parse_command_line():
    """
    Parses the command-line arguments.
    :return: The parsed arguments.
    """
    parser = argparse.ArgumentParser(description='Read the contents of a .torrent file.')
    parser.add_argument('torrent_file_path', metavar='path', type=str, nargs='+',
                        help='the path to the torrent file')
    parser.add_argument('--verbose', action='store_true',
                        help='show additional information about the torrent file')
    args = parser.parse_args()

    return parser.torrent_file_path, parser.verbose


def print_torrent_file_contents(torrent, is_verbose):
    """
    Prints the contents of a torrent file.
    :param torrent: the Torrent object.
    :param is_verbose: whether to display more information than normal.
    :return: None
    """

    print("Tracker URL: %s" % torrent.announce)
    print("Tracker List: %s" % torrent.announce_list)
    print("Creation Date: %s" % torrent.creation_date.isoformat() if torrent.creation_date else None)
    print("Created By: %s" % torrent.created_by)
    print("Comment: %s" % torrent.comment)
    print("No External Peer Source: %s" % torrent.info.private)

    if is_verbose:
        print("Encoding: %s" % torrent.encoding)
        print("Size per Piece: %d" % torrent.info.piece_length)
        print("Pieces: %s" % torrent.info.pieces)

    # Single File Mode.
    if torrent.info.md5sum or torrent.info.length:
        print("File Path: %s" % torrent.info.name)
        print("File Size: %d" % torrent.info.length)
        print("File Checksum: %s" % torrent.info.md5sum)

    # Multiple File Mode.
    else:

        print("Directory: %s" % torrent.info.name)
        for torrent_file in torrent.info.files:
            # Multiple file mode.
            print("File Path: %s" % torrent_file.path)
            print("File Size: %d" % torrent_file.length)
            print("File Checksum: %s" % torrent_file.md5sum)