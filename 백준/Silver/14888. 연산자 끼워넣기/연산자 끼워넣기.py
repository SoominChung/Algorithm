
from itertools import permutations

N = int(input())
number = list(map(int, input().split()))
p,m,s,d = map(int,input().split())
total_calc = []
for _ in range(p):
    total_calc.append(0)
for _ in range(m):
    total_calc.append(1)
for _ in range(s):
    total_calc.append(2)
for _ in range(d):
    total_calc.append(3)

def calculataion(cc, x,y):
    if cc == 0:
        return x+y
    elif cc == 1:
        return x-y
    elif cc == 2:
        return x*y
    else:
        if x>=0:
            return x // y
        else:
            #return -1*x // y * (-1)
            return int(x/y)

cases = list(set(permutations(total_calc,N-1)))
min_val, max_val = 1e9+2,-1e9-4
for case_ in cases:
    # 하나의 케이스에 대해

    # 함수 활용해서 생으로 계산할 때
    tmp = number[0]
    for i in range(1,N):
        tmp = calculataion(list(case_)[i-1], tmp, number[i])


    min_val, max_val = min(min_val, tmp), max(max_val, tmp)
print(max_val)
print(min_val)