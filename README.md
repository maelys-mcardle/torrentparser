# BitTorrent Parser
A native Python implementation of a BitTorrent file parser.

# Current Build Status
[![Build Status](https://travis-ci.org/maelys-mcardle/torrentparser.svg?branch=master)](https://travis-ci.org/maelys-mcardle/torrentparser)

# Author
Maelys McArdle ([maelys.bio](http://maelys.bio))

# License
MIT

# Installation

### Notes

The implementation was tested on `Fedora 25` against `Python 2.7.12`.

The instructions assumed `pip` is installed, which comes standard with `Python 2 >= 2.7.9`.
It also assumes your current wording directory is the project directory.

### Installation

To install the `torrentparser` package, run the following command:

    pip install .
    
### Uninstallation
To uninstall the package, run the following command:

    pip uninstall torrentparser

### Running Tests

To run tests, run the following command:

    python setup.py test
    
# Using the Module

To read the contents of a torrent file, use the `parse_torrent_file`:

    from torrentparser.parser import parse_torrent_file
    
    # Load the torrent file.
    torrent = parse_torrent_file("some_torrent_file.torrent")
    
    # Show the tracker url.
    print(torrent.announce)
    
    # Show the creation date.
    # Dates are stored using Python's datetime object.
    print(torrent.creation_date.isoformat())
    
    # Show the client that created the file.
    print(torrent.created_by)
    
    # Show info about a single file (single file mode).
    print(torrent.info.name)
    print(torrent.info.checksum)
    print(torrent.info.checksum_type)
    print(torrent.info.length)
    
    # Show info about multiple files (multiple file mode).
    for torrent_file in torrent.info.files:
        print(torrent_file.path)
        print(torrent_file.checksum)
        print(torrent_file.checksum_type)
        print(torrent_file.length)

        
If there was an error parsing the torrent file, a `Torrent.Error` exception will be raised:

    from torrentparser.parser import parse_torrent_file
    from torrentparser.torrent import Torrent
    
    # Load the torrent file.
    try:
        torrent = parse_torrent_file("some_torrent_file.torrent")
        
    # If there was an error parsing the file, display the reason.
    except Torrent.Error as error_message:
        print(error_message)
    
        
The file's data can also be obtained as a native Python dictionary with the
`parse_torrent_file_as_dictionary` function.

    from torrentparser.parser import parse_torrent_file_as_dictionary
    
    # Load the torrent file.
    torrent = parse_torrent_file_as_dictionary("some_torrent_file.torrent")
    
    # The function will not raise an exception if it cannot parse the file.
    # Instead, it will return an empty dictionary.
    
    if not torrent:
        print("Failed to parse the torrent file!")
    
    else:
    
        # Show the tracker url.
        print(torrent["announce"])
        
        # Show the creation date.
        # The value will be in UNIX time.
        print(torrent["creation date"])
        
        # Show the client that created the file.
        print(torrent["created by"])
        
        # Show info about a single file (single file mode).
        print(torrent["info"]["name"])
        print(torrent["info"]["md5"])
        print(torrent["info"]["length"])
        
        # Show info about multiple files (multiple file mode).
        for torrent_file in torrent["info"]["files"]:
            print(torrent_file["path"])
            print(torrent_file["md5"])
            print(torrent_file["length"])


# Using The Command-Line

The command `show_torrent_info` is provided to open torrent files from the command-line.

It's available upon the installation of the `torrentparser` module.

    # Show the command-line options.
    show_torrent_info --help
        
    # Show information contained in the torrent file. 
    show_torrent_info /path/to/file.torrent
    
    # Show more information stored in the torrent file.
    show_torrent_info /path/to/file.torrent --verbose
    
Example usage:

    show_torrent_info tests/sample/v1publicacc1985canauoft_archive.torrent 
    
    INFO
      Tracker URL:   http://bt1.archive.org:6969/announce
      Tracker List:  [['http://bt1.archive.org:6969/announce'], ['http://bt2.archive.org:6969/announce']]
      Creation Date: 2016-05-14T09:31:09
      Created By:    None
      Private:       None
      Comment:       This content hosted at the Internet Archive at https://archive.org/details/v1publicacc1985canauoft
    Files may have changed, which prevents torrents from downloading correctly or completely; please check for an updated torrent at https://archive.org/download/v1publicacc1985canauoft/v1publicacc1985canauoft_archive.torrent
    Note: retrieval usually requires a client that supports webseeding (GetRight style).
    Note: many Internet Archive torrents contain a 'pad file' directory. This directory and the files within it may be erased once retrieval completes.
    Note: the file v1publicacc1985canauoft_meta.xml contains metadata about this torrent's contents.
    
    FILE LISTING
      Directory: v1publicacc1985canauoft
      'scandata.zip'
        Size:     53836494 bytes
        Checksum: cb5ba74f06a2ed19d9a558b8d31a0287db7dae63 (Type: SHA1)
    
      'v1publicacc1985canauoft.djvu'
        Size:     12970369 bytes
        Checksum: 4ece9941257681116a9c1b2bb801ffcc89b42784 (Type: SHA1)
    
      'v1publicacc1985canauoft.gif'
        Size:     318858 bytes
        Checksum: a39776a2a16ee1071a1b540aff903f2749d7418f (Type: SHA1)


    ...