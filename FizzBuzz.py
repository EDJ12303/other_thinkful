# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 22:34:37 2016

@author: Erin
"""

def F(n):
    if n < 2:
        print (n)
        return n        
    else:
        print (F(n-2) + F(n-1))
        return F(n-2) + F(n-1)