#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 2024

@author: Enochneier
"""
import json


def to_json_string(my_obj):
    """
    Returs a json string containing object's representation

    Arguments:
        my_obj (str): The inputed object to convert in json format

    Return:
        A json format text
    """
    return json.dumps(my_obj)
