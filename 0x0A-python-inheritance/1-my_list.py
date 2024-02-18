#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 2024

@author: Enochneier
"""


class MyList(list):
    """
     class MyList that inherits from list
    """
    def print_sorted(self):
        """
        Public instance method that prints sorted list
        """
        list_copy = self[:]
        list_copy.sort()
        print(list_copy)
