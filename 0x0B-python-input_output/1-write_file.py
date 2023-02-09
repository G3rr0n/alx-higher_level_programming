#!/usr/bin/python3
"""defining a file-writing method."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 format txt file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
