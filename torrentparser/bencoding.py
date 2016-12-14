"""
Bencoding decoding functions.
"""


def decode_byte_string(encoded_byte_string):
    """
    Decodes a Bencoding byte string.
    :param encoded_byte_string: The byte string in Bencoding.
    :return: Tuple containing the byte string and the size of the encoded string.
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
            byte_string_start, byte_string_end = delimiter_position + 1, delimiter_position + 1 + string_size_as_integer

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
    :return: Tuple containing the integer and the size of the encoded integer.
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
    :param encoded_list: The list in Bencoding.
    :return: Tuple containing the list and the size of the encoded list.
    """

    # First byte needs to be a "l" to signify that it's a Bencoding list.
    if len(encoded_list) == 0 or encoded_list[0] != "l":
        raise BencodingDecodeException("Not a list")

    # Initialize an empty list.
    decoded_list = list()
    start_position = 1

    # Continue reading until the end.
    while True:

        # Start position unreadable.
        if start_position >= len(encoded_list):
            raise BencodingDecodeException("Invalid list (missing data)")

        # List is finished.
        if encoded_list[start_position] == "e":
            break

        # There's a list item. Decode it.
        else:
            item, encoded_size = decode_item(encoded_list[start_position:])
            start_position += encoded_size
            decoded_list.append(item)

    return decoded_list, start_position + 1


def decode_dictionary(encoded_dictionary):
    """
    Decodes a Bencoding dictionary.
    :param encoded_dictionary: The dictionary in Bencoding.
    :return: Tuple containing the dictionary and the size of the encoded dictionary.
    """

    # First byte needs to be a "d" to signify that it's a Bencoding dictionary.
    if len(encoded_dictionary) == 0 or encoded_dictionary[0] != "d":
        raise BencodingDecodeException("Not a dictionary")

    # Initialize a dictionary.
    start_position = 1
    decoded_dictionary = dict()

    # Continue reading until the end.
    while True:

        # Start position unreadable.
        if start_position >= len(encoded_dictionary):
            raise BencodingDecodeException("Invalid dictionary (missing data)")

        # Dictionary is finished.
        if encoded_dictionary[start_position] == "e":
            break

        # Decode the dictionary key/value pair.
        else:

            # Grab the key.
            key, key_size = decode_item(encoded_dictionary[start_position:])

            # Value unreadable.
            if start_position+key_size >= len(encoded_dictionary):
                raise BencodingDecodeException("Invalid dictionary (missing data)")

            # Grab the value.
            value, value_size = decode_item(encoded_dictionary[start_position+key_size:])
            start_position += key_size + value_size

            # Load it in the dictionary.
            decoded_dictionary[key] = value

    return decoded_dictionary, start_position + 1


def decode_item(encoded_item):
    """
    Decodes the items found in a list or dictionary.
    :param encoded_item: The encoded item (byte string, integer, list, dict).
    :return: A tuple containing the decoded item and the size of the encoded item.
    """
    first_byte = encoded_item[0]

    # Item is an integer.
    if first_byte == "i":
        return decode_integer(encoded_item)

    # Item is a list.
    elif first_byte == "l":
        return decode_list(encoded_item)

    # Item is a dictionary.
    elif first_byte == "d":
        return decode_dictionary(encoded_item)

    # Item is a byte string.
    elif first_byte.isdigit():
        return decode_byte_string(encoded_item)

    # Unknown item.
    else:
        raise BencodingDecodeException("Unrecognized item (type: %s)" % first_byte)


class BencodingDecodeException(Exception):
    """
    Exception raised during decoding of data encoded with Bencoding.
    """
    pass
