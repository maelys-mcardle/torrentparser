"""
Provides a command-line interface to show the contents of torrent files.
"""
import argparse
from os import sep as directory_separator
from binascii import hexlify
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
    parser.add_argument('torrent_file_path', metavar='path', type=str,
                        help='the path to the torrent file')
    parser.add_argument('--verbose', action='store_true',
                        help='show additional information about the torrent file')
    args = parser.parse_args()

    return args.torrent_file_path, args.verbose


def print_torrent_file_contents(torrent, is_verbose):
    """
    Prints the contents of a torrent file.
    :param torrent: the Torrent object.
    :param is_verbose: whether to display more information than normal.
    :return: None
    """

    print("INFO")
    print("  Tracker URL:   %s" % torrent.announce)
    print("  Tracker List:  %s" % torrent.announce_list)
    print("  Creation Date: %s" % torrent.creation_date.isoformat() if torrent.creation_date else None)
    print("  Created By:    %s" % torrent.created_by)
    print("  Private:       %s" % torrent.info.private)
    print("  Comment:       %s\n" % torrent.comment)

    if is_verbose:
        print("PIECES")
        print("  Encoding:       %s" % torrent.encoding)
        print("  Size per Piece: %d" % torrent.info.piece_length)
        print("  Pieces: %s\n" % hexlify(torrent.info.pieces))

    # Single File Mode.
    print("FILE LISTING")
    if torrent.info.checksum or torrent.info.length:

        print("  '%s'" % torrent.info.name)
        print("    Size:     %d bytes" % torrent.info.length)
        print("    Checksum: %s (Type: %s)\n" % (torrent.info.checksum, torrent.info.checksum_type))

    # Multiple File Mode.
    else:

        print("  Directory: %s" % torrent.info.name)
        for torrent_file in torrent.info.files:
            # Multiple file mode.
            print("  '%s'" % directory_separator.join(torrent_file.path))
            print("    Size:     %d bytes" % torrent_file.length)
            print("    Checksum: %s (Type: %s)\n" % (torrent_file.checksum, torrent_file.checksum_type))
