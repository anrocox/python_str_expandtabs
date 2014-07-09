#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 9, 2014

@author: anroco

In python how to change the tabs by spaces in a string?

En python ¿como cambiar los tabs de un string por espacios?
'''

#create a str
s = '\tdef function(x, y)\n\t\treturn x + y\n'
print(s)

#generates a copy of 's' where all tab characters are replaced by one or
#more spaces.
#Tab positions occur every tabsize characters (default is 8, giving tab
#positions at columns 0, 8, 16, 24 and so on).
#show full documentation in https://docs.python.org/3/library/stdtypes.html#str
s_tab_space = s.expandtabs(3)
print(s_tab_space)
