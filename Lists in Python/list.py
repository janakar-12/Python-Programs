n = int(input())
l = []

for i in range(n):
    query = input()
    query_lst = query.split(" ")
    
    if query_lst[0] == 'insert':
        l.insert(int(query_lst[1]), int(query_lst[2]))
        
    elif query_lst[0] == 'print':
        print(l)
    
    elif query_lst[0] == 'remove':
        l.remove(int(query_lst[1]))
        
    elif query_lst[0] == 'pop':
        l.pop()
        
    elif query_lst[0] == 'append':
        l.append(int(query_lst[1]))
        
    elif query_lst[0] == 'reverse':
        l.reverse()
    
    elif query_lst[0] == 'sort':
        l = sorted(l)
