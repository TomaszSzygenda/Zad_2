# -*- coding: utf-8 -*-
"""
Created on Fri May  7 18:54:30 2021
@author: Tomasz_Szygenda
"""

def srednia(x,y):
    if x>0 and y>x:
        suma_niepodzielnych=0
        suma=0;
        
        for a in range(x,y+1):
            if a%2:
                suma_niepodzielnych+=1
                suma=suma+a
        print("renia arytmetyczna z liczb nieparzystych z przedziału:",x,y,"jest równa:",suma/suma_niepodzielnych)

    else:

        print("proszę podać prawidłowy przedział")
            
    
   
    
   
    
x=input("Wypisz początek przedziału:")
y=input("Wypisz koniec przedziału:")

srednia(int(x),int(y))
    
