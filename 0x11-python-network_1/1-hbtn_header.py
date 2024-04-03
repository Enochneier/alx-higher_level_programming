#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed 4 Apr 2024

@author: Enochneier
"""
from urllib.request import urlopen
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    with urlopen(url) as response:
        info = response.info()
        print(info['X-Request-Id'])
