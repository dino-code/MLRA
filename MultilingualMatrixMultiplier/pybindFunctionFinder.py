#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 15:46:18 2020

@author: dinobecaj
"""

import os



currDirectory = os.getcwdb()

for root, names, filenames in os.walk(currDirectory):
    print("filenames:", filenames)