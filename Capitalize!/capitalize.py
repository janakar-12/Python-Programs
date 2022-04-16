# Solution 1
import math
import os
import random
import re
import sys

def solve(s):
    for i in s.split():
        s = s.replace(i, i.capitalize())
    return s

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
    
# Solution 2

'''def solve(s):    
    lst = []
    l = s.split(' ')
    for i in l:
        e = i[0].upper() + i[1:]
        lst.append(e)
    s = ' '.join(lst)
    
    return s


s = input()
result = solve(s)
print(result)'''
