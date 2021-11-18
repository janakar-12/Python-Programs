a, b = [int(_) for _ in input().split(' ')]
mid = (a // 2)
des1 = '.|.'
c = 1
for _ in range(1, mid+1):
    des2 = des1 * c
    print(des2.center(b, '-'))
    if _ != mid:
        c += 2
print('WELCOME'.center(b, '-'))
for i in range(mid, 0, -1):
    des2 = des1 * c
    print(des2.center(b, '-'))
    c -= 2
