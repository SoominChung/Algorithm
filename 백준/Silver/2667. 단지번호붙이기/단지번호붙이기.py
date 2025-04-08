from collections import deque

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int,input())))

danzi = []
for i in range(N):
    danzi.append([-1]*N)
# danzi = [[-1]*N]*N => 모든 행이 같은 리스트 객체를 참조하므로 danzi[x][y] = 1 로 바꿔도 모든 열이 동일하게 바뀜. 주의!!!!
count = 0
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y,cnt):
    q = deque([(x,y)])
    danzi[x][y] = cnt
    cnt_num = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if (0<=nx<N) and (0<=ny<N) and (graph[nx][ny] == 1) and (danzi[nx][ny] == -1): # danzi[nx][ny] == -1 이 조건이 없으면 무한루프로 들어감 (방문한곳은 안가도되지)
                q.append((nx,ny))
                danzi[nx][ny] = cnt
                cnt_num += 1
    return cnt_num

cnt_dict = {}
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and danzi[i][j] == -1:
            count += 1
            cnt_dict[count] = bfs(i,j,count)

print(count)
for i in sorted(cnt_dict.values()):
    print(i)