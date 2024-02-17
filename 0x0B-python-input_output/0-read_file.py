#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 2024

@author: Enochneier
"""


def read_file(filename=""):
    """
    Reads the file

    Arguments:
        filename (str): The name of the file to open
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
