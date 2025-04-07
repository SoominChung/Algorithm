# 최단거리를 묻고, 간선의 가중이 모두 동일하니 BFS로 해결   
# 첫트: 시간초과 -> readline 사용
from collections import deque
import sys

#n, m, k, x = map(int,input().split())
n,m,k,x = list(map(int, sys.stdin.readline().split()))

# 전체 도로 정보 (단방향 도로를 인접 리스트로 표현)
graph = [[] for _ in range(n+1)]
for i in range(m):
    #a,b = map(int, input().split())
    a,b = list(map(int, sys.stdin.readline().split()))
    graph[a].append(b)

# 도시별 x부터의 거리 저장
distance = [-1]*(n+1)
distance[x] = 0

queue = deque([x])
while queue:
    # 현재 도시
    now = queue.popleft()
    
    # 인접 도시들에 대해 거리 저장
    for i in graph[now]:
        # 처음 방문한 도시라면 거리 저장해주고 queue에 넣음
        if distance[i]==-1:
            distance[i] = distance[now]+1
            queue.append(i)

check = False            
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        check =True
if check ==False:
    print(-1)