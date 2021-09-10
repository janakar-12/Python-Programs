arr = [] 
spliting = []
ans = []

for i in range(6):
    l = list(map(int, input().strip().split()))
    arr.append(l)
    
a = x = 0
b = y = 1
c = 2

for i in range(4):
    if a < 4 and c < 6 and b < 5:
        for j in range(4):
            if x < 4 and y < 5:
                sub = [arr[a][x], arr[a][x+1], arr[a][x+2], arr[b][y], arr[c][x], arr[c][x+1], arr[c][x+2]]
                spliting.append(sub)
            x += 1
            y += 1
    a += 1
    b += 1
    c += 1
    x = 0
    y = 1
  
for i in spliting:
    ans.append(sum(i))
print(max(ans))
