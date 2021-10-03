n = list(map(int, input().strip().split()))
last_answer = 0
l = []

for i in range(n[0]):
    l.append(list())

for i in range(n[1]):
    query = list(map(int, input().strip().split()))
    
    if query[0] == 1:
        
        idx = (query[1] ^ last_answer) % n[0]
        appen = l[idx]
        appen.append(query[2])
        
    else:
        
        idx = (query[1] ^ last_answer) % n[0]
        idx2 = query[2] % len(l[idx])
        
        last_answer = l[idx][idx2]
        print(last_answer)
