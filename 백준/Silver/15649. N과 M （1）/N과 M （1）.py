# N과 M (1) - 백준 15649

N, M = map(int, input().split())

arr = []               # 현재 수열을 저장할 리스트
used = [False] * (N+1) # 각 숫자가 사용됐는지 체크 (1~N)

def dfs(depth):
    if depth == M:
        print(*arr)
        return
    
    for i in range(1, N+1):
        if not used[i]:       # 아직 사용하지 않은 숫자라면
            arr.append(i)     # 수열에 추가
            used[i] = True    # 사용 처리
            dfs(depth + 1)    # 다음 깊이로 재귀 호출
            arr.pop()         # 수열에서 제거 (백트래킹)
            used[i] = False   # 사용 처리 해제 (백트래킹)

dfs(0)
