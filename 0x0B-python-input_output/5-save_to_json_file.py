#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 2024

@author: Enochneier
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Save object to a file

    Arguments:
        my_obj (obj): The inputed object to convert in json format
        filename (str): The name of the output file

    Return:
        A file with a text in jason format
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(json.dumps(my_obj))
