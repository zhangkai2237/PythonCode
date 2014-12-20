# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 22:49:24 2014

@author: Kevin
"""
import math;

a = int(raw_input());
b = int(raw_input());
c = int(raw_input());

print format((math.sqrt(1-((a**2+b**2-c**2)/(2.0*a*b))**2)*90),"0.1f")