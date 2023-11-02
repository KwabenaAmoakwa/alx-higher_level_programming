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
    new_str = text.split()
    text = "|".join(new_str)
    new_str = ""
    for i in text:
        if i == "|":
            continue
        if i in ".?:":
            new_str += i + "|"
        else:
            new_str += i
    ns = new_str.split("| ")
    print("\n\n".join(ns), end="")
