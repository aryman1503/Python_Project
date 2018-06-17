# -*- coding: utf-8 -*-
"""
Created on Tue May 22 22:11:03 2018

@author: aryman
"""
print("\t\t--Table--")
x=int(input("Please Enter the Number whose table you want to see ::: "))
print()
for i in range(11) :
    if i == 0:
        pass
    else:
        print(repr(x).rjust(25),"X",i," =",repr(x*i))
        
print()
exit=input("Press Enter for Exit")
    
