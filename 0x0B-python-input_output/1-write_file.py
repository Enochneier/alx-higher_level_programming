#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 2024

@author: Enochneier
"""


def write_file(filename="", text=""):
    """
    Counts the number of lines from the filename

    Arguments:
        filename (str): The name of the file to open
        text (str): The text to write in

        Return:
            A file with text written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
