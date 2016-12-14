"""
Bencoding decoding functions.
"""


def decode_byte_string(encoded_byte_string):
    """
    Decodes a Bencoding byte string.
    :param encoded_byte_string: The byte string in Bencoding.
    :return: Tuple containing the byte string and the end byte index.
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


def decode_integer(encoded_integer):
    """
    Decodes a Bencoding integer.
    :param encoded_integer: The integer in Bencoding.
    :return: Tuple containing the integer and the end byte index.
    """

    # First byte needs to be a "i" to signify that it's a Bencoding integer.
    if len(encoded_integer) == 0 or encoded_integer[0] != "i":
        raise BencodingDecodeException("Not an integer")

    # Find the end.
    end_position = encoded_integer.find("e")

    # There wasn't an end.
    if end_position == -1:
        raise BencodingDecodeException("Invalid integer (missing terminating 'e')")

    # Get the integer.
    integer_as_string = encoded_integer[1:end_position]

    # If the string is empty, indicate an error.
    if len(integer_as_string) == 0:
        raise BencodingDecodeException("Invalid integer (missing value)")

    # Try parsing the integer. If it's valid, return it.
    try:
        integer = int(integer_as_string)
        return integer, end_position + 1

    # Value is invalid, indicate error.
    except ValueError:
        raise BencodingDecodeException("Invalid integer (not a number)")


def decode_list(encoded_list):
    """
    Decodes a Bencoding list.
    :param encoded_list:
    :return:
    """

    # First byte needs to be a "l" to signify that it's a Bencoding list.
    if len(encoded_list) == 0 or encoded_list[0] != "l":
        raise BencodingDecodeException("Not a list")

    # Initialize an empty list.
    decoded_list = list()
    start_position = 1

    # Continue reading.
    while True:

        # Start position unreadable.
        if start_position >= len(encoded_list):
            raise BencodingDecodeException("Invalid list (missing data)")

        #
        first_byte = encoded_list[start_position]

        # List is finished.
        if first_byte == "e":
            break

        # List item: integer.
        elif first_byte == "i":

        # List item: nested list.
        elif first_byte == "l":

        # List item: dictionary.
        elif first_byte == "d":

        # List item: byte string.
        elif first_byte.isdigit():

        # Unknown list item.
        else:


def is_byte_string(encoded_byte_string):
    """
    Convenience function to identify whether it's a byte string.
    :param encoded_byte_string: The byte string in Bencoding.
    :return: Boolean indicating if this is a byte string.
    """

    try:
        decode_byte_string(encoded_byte_string)
        return True
    except BencodingDecodeException:
        return False


def is_integer(encoded_integer):
    """
    Convenience function to identify whether it's an integer.
    :param encoded_integer: The integer in Bencoding.
    :return: Boolean indicating if this is an integer.
    """

    try:
        decode_integer(encoded_integer)
        return True
    except BencodingDecodeException:
        return False


def decode_dictionary(encoded_dictionary):
    """
    Decodes Bencoding dictionaries.
    """

    # First byte needs to be a "d" to signify that it's a Bencoding dictionary.
    if len(encoded_dictionary) == 0 or encoded_dictionary[0] != "d":
        raise BencodingDecodeException("Not a dictionary")

    start_position = 1
    decoded_dictionary = dict()

    # Continue reading.
    while True:

        # Start position unreadable.
        if start_position >= len(encoded_dictionary):
            raise BencodingDecodeException("Invalid dictionary (missing data)")

        # Dictionary is finished.
        if encoded_dictionary[start_position] == "e":
            break

        # Read

    return decoded_dictionary


class BencodingDecodeException(Exception):
    """
    Exception raised during decoding of data encoded with Bencoding.
    """
    pass

