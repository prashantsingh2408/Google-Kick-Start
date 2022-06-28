t  = int(input())
r = []
for i in range(t):
    b,k = map(int,input().split())
    c = list(map(int,input().split()))
    sum_inner =0
    for j in c:
        sum_inner += j
    r.append(sum_inner % k)
for i,j in enumerate(r):
    print('Case #{}: {}'.format(i+1,j))

