N = int(input())
number = list(map(int, input().split()))
p,s,m,d = map(int,input().split())

min_val,max_val = 2e9,-2e9

def dfs(depth,num,plus,substract,multiply,divide):
    global min_val, max_val
    if depth == N: # 끝까지 탐색해야지
        min_val = min(min_val,num)
        max_val = max(max_val,num)
        return

    if plus:
        dfs(depth+1,num+number[depth],plus-1,substract,multiply,divide)
    if substract:
        dfs(depth+1,num-number[depth],plus,substract-1,multiply,divide)
    if multiply:
        dfs(depth+1,num*number[depth],plus,substract,multiply-1,divide)
    if divide:
        if num <0:
            dfs(depth+1,-(-num//number[depth]),plus,substract,multiply,divide-1)
        else:
            dfs(depth+1,num//number[depth],plus,substract,multiply,divide-1)

dfs(1, number[0], p,s,m,d)
print(max_val)
print(min_val)