'''
L,R
2,2
 ()()
 2 + 1 = 3(maxinum balance substring '()','()','()()')
2,3
 (()()
  2+1 = 3
4,4
  ()()()()
  4 + 2 = 5
6,6
 ()()()()()()
 5+3+2 = 10
'''
def result(l,r):
    #empty string
    if l ==0 and r == 0:
        return 1
    res = 0 #result
    m = min(l,r)
    res = m
    div = 2
    while True:
        if (m // div) > 0:
            res = res + (m // div)
            div = div + 1
        else:
            break
    return res
def output(res):
    for index,i in enumerate(res):
        print("Case #{}: {}".format(index+1,i))

t = int(input())
res = []
for i in range(t):
    l,r = map(int,input().split())
    res.append(result(l,r))
output(res)
    
