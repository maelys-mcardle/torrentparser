
def decode_byte_string(encoded_byte_string):
    """Decodes Bencoding byte strings.

    Byte strings have the format:
        <string length encoded in base ten ASCII>:<string data>

    Example:
        5:hello
    """

    # Find the colon.
    delimiter_position = encoded_byte_string.find(":")

    # Colon doesn't exist.
    if delimiter_position == -1:
        raise BencodingDecodeException("Invalid byte string (missing a colon)")

    # Colon exists.
    else:

        # Get the base ten ASCII string size.
        string_size_as_string = encoded_byte_string[:delimiter_position]

        # If the ASCII string size is not made of digits, indicate an error.
        if not string_size_as_string.isdigit():
            raise BencodingDecodeException("Invalid byte string (size contains non-numeric characters)")

        # If the ASCII string size is made up of digits, proceed.
        else:

            # Interpret the size as an integer.
            string_size_as_integer = int(string_size_as_string)

            # Calculate where the byte string actually starts and ends in the encoded data.
            byte_string_start, byte_string_end = delimiter_position+1, delimiter_position+1+string_size_as_integer

            # If the end exceeds the boundaries of the input, indicate an error.
            if byte_string_end > len(encoded_byte_string):
                raise BencodingDecodeException("Invalid byte string (missing data)")

            # Otherwise return the string.
            else:
                decoded_byte_string = encoded_byte_string[byte_string_start:byte_string_end]
                return decoded_byte_string, byte_string_end


def decode_dictionary(dictionary):
    """Decodes Bencoding dictionaries.

    Dictionaries have the format:
        d<string length encoded in base ten ASCII>:<string data>e

    Example:
        d3:cow3:moo4:spam4:eggse
    """
    # First byte needs to be a "d" to signify that it's a Bencoding dictionary.
    if dictionary[0] != "d":
        raise BencodingDecodeException("Not a dictionary.")

    return dict()


class BencodingDecodeException(Exception):
    """Exception raised during decoding of data encoded with Bencoding.
    """
    pass

