
N, M = map(int, input().split())

used = [False for _ in range(N+1)]
arr = []
def dfs(depth):
    if depth == M:
        print(*arr)
        return

    for i in range(1,N+1):
        if not used[i]:
            if len(arr) == 0:
                arr.append(i)
                used[i] = True
                dfs(depth+1)
                used[i] = False
                arr.pop()
            else:
                if arr[-1]<i:
                    arr.append(i)
                    used[i] = True
                    dfs(depth+1)
                    used[i] = False
                    arr.pop()                    
dfs(0)