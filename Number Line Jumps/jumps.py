samp = list(map(int, input().strip().split()))

k1 = samp[:2]
k2 = samp[2:]
c = 0


if sum(k1) == sum(k2):
    print('YES')
elif k1[0] < k2[0] and k1[1] <= k2[1]:
    print('NO')
elif k1[0] > k2[0] and k1[1] > k2[1]:
    print('NO')
elif (k1[0] - k2[0]) % (k1[1] - k2[1]) == 0 or (k1[0] - k2[0]) % (k2[1] - k1[1]) == 0:
    print('YES')
else:
    print('NO')
