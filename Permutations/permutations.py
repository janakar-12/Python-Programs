from itertools import permutations

l = list(map(str, input().strip().split()))

l1 = list(permutations(l[0], int(l[1])))
ans = sorted(l1)

for i in(ans):
    print(''.join(i))
