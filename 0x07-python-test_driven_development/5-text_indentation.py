#!/usr/bin/python3
"""text_identication module"""


def text_indentation(text):
    """Split the text into paragraphs based on the delimiters '.','?', and ':'

    The function takes a string `text` as input and splits it into paragraphs
    based on the presence of the delimiters '.', '?', and ':'. The resulting
    paragraphs are printed with two newline characters between them.

    Args:
        text (str): The input text to be split into paragraphs.

    Returns:
        None
    """
    if not type(text) is str:
        raise TypeError("text must be a string")

    new_str = text.split(" ")
    text = "|".join(new_str)
    new_str = ""
    for index, value in enumerate(text):
        if value == "|" and text[index - 1] not in ":.?|":
            if text[index + 1] == " ":
                new_str += " "
        elif value in ".?:":
            new_str += value + "|"
        elif value != "|":
            new_str += value
    ns = new_str.split("|")
    print("\n\n".join(ns), end="")
