n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

for i in range(n):

    for j in range(1, 5):
        
        if lst[i] < 38:
            break
        a = lst[i] + j
        if a % 5 == 0:
            if a - lst[i] < 3:
                lst[i] = a
            else:
                break

for i in(lst):
    print(i)
