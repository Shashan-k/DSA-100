"""
*****
*****
*****
*****
*****  
"""

for i in range(5):
    for j in range(5):
       
        print("*",end = ' ')
    print(" ")
    
    
    
"""
*
**
***
****
*****  
"""

for i in range(5):
    for j in range(i+1):
        print("*", end = ' ')
        
    print(" ")
  
    
"""
*****  
****
***
**
*
"""

print("Pattern 3")

n=5
for i in range(n):
    for j in range(n):
        print("*", end = " ")
    
    print(" ")    
    n = n-1
