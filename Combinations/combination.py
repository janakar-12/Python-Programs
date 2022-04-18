from itertools import combinations

ans = []
l = list(map(str, input().strip().split()))

for i in range(1, int(l[1])+1):
    lst = list(combinations(l[0], i))
    
    for j in lst:
        e = ''.join(sorted(j))
        ans.append(e)
    ans.sort()
    for k in ans:
        print(k)
    lst.clear()
    ans.clear()
