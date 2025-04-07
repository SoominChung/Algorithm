import copy
from itertools import combinations, permutations
from collections import deque
n, m = map(int, input().split())

maps = []
empty_indicies = [] # 빈 공간의 인덱스
virus_indicies = deque() # 바이러스의 인덱스 -> deque로 미리 선언해두기!
for i in range(n):
    maps.append(list(map(int, input().split())))
    for j in range(m):
        if maps[i][j] == 0:
            empty_indicies.append((i, j))
        elif maps[i][j] == 2:
            virus_indicies.append((i, j))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

max_safe_area = 0
# 3개 벽을 세울 수 있는 모든 조합
possible_empty_indices = combinations(empty_indicies,3)
for indices in possible_empty_indices:
    tmp_maps = copy.deepcopy(maps)
    
    # 벽 세우기
    for i in indices:
        tmp_maps[i[0]][i[1]] = 1
    
    # 바이러스 퍼뜨리기
    tmp_virus_indicies = copy.deepcopy(virus_indicies)
    while tmp_virus_indicies:
        x, y = tmp_virus_indicies.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and tmp_maps[nx][ny] == 0:
                tmp_maps[nx][ny] = 2
                tmp_virus_indicies.append((nx, ny))
        
    # 안전영역 계산
    tmp_safe_area = 0
    for i in range(n):
        tmp_safe_area += tmp_maps[i].count(0)

    max_safe_area = max(max_safe_area, tmp_safe_area)

print(max_safe_area)