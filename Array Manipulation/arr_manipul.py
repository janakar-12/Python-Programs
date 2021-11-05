A, B = [int(_) for _ in input().split(' ')]

val = {}

for i in range(B):
    a, b, k = [int(_) for _ in input().strip().split(' ')]
    if k == 0:
        continue
    val[a] = val.get(a, 0) + k
    val[b+1] = val.get(b+1, 0) - k
    
x, y = 0, 0

for i in sorted(val):
    y += val[i]
    if y > x:
        x = y

print(x)
