# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 22:43:24 2014

@author: Kevin
"""

inputSec = int(raw_input());

second = inputSec % 60

inputMin = inputSec / 60

minValue = inputMin % 60

hour = inputMin / 60

print hour, minValue, second