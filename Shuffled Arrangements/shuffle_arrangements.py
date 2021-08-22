import random
import math

n = int(input())
l = []
c = 0

for i in range(n):
    ele=input()
    l.append(ele)
    
for i in range(n):
    
    l1 = []
    lstt = l[i]
    lst = list(lstt)
   
    f = math.factorial(len(lst))
    lstcpy = lst.copy()
    
    for i in range(f):
        
        x = 0
        random.shuffle(lstcpy)
        
        for j in range(len(lst)):
        
            if lst[j] != lstcpy[j]:
                x += 1
                
        if x == len(lst):
            lst1 = "".join(lstcpy)
            l1.append(lst1)            
        
    if len(l1) == 0:
        c += 1
        print('Case','#'+str(c)+':','IMPOSSIBLE')
    else:
        c += 1
        print('Case','#'+str(c)+':',l1[0])
    lst.clear()
