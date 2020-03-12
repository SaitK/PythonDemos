# -*- coding: utf-8 -*-
from __future__ import unicode_literals
a = 0
lst = range(2,10)

while (a < len(lst)):
    if (lst[a] % 2 == 0 ):
        print (lst[a])
        
    a = a+1
    continue