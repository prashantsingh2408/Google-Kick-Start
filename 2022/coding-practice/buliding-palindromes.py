"""
2
7 5
ABAACCA
3 6
4 4
2 5
6 7
3 7
3 5
XYZ
1 3
1 3
1 3
1 3
1 3
-------------
Case #1: 3
Case #2: 0
----------
In Sample Case #1, N = 7 and Q = 5.

For the first question, Anna must use the blocks AACC. She can rearrange these blocks into the palindrome ACCA (or CAAC).
For the second question, Anna must use the blocks A. This is already a palindrome, so she does not need to rearrange them.
For the third question, Anna must use the blocks BAAC. These blocks cannot be rearranged into a palindrome.
For the fourth question, Anna must use the blocks CA. These blocks cannot be rearranged into a palindrome.
For the fifth question, Anna must use the blocks AACCA. She can rearrange these blocks to form the palindrome ACACA (or CAAAC).
In total, she is able to answer "yes" to 3 of Bob's questions, so the answer is 3.
In Sample Case #2, N = 3 and Q = 5. For the first question, Anna must use the blocks XYZ to create a palindrome. This is impossible, and since the rest of Bob's questions are the same as the first one, the answer is 0.


"""
def output(res):
    for index,i in enumerate(res):
        print("Case #{}: {}".format(index+1,i))

t = int(input())
t = int(input())
res = []

for i in range(t):
    n, q = map(int,input().split())
    str = input()
    ans_yes = 0
    for j in range(q):
        l, r = map(int,input().split())
        sub_str = str[l:r+1]
        if(ifPelendromePossible(sub_str)):
           ans_yes = ans_yes + 1
    res.append(ans_yes)


output(res)


