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
        filename (str): The name of the file to count in
    """
    with open(filename, "w+") as file:
        file.write("")
        file.close()

    with open(filename, encoding='utf-8') as file:
        lines = file.readlines()
    return len(lines)
