#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed 4 Apr 2024

@author: Enochneier
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    response = get(url)
    info = response.headers
    print(info.get('x-request-id'))
