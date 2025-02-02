import sys
from collections import deque
input = sys.stdin.readline

M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)]
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
queue = deque()
area_list = []

for _ in range(K):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(ly, ry):
        for j in range(lx, rx):
            arr[i][j] = 1

# bfs 돌면서 0인 부분 넓이 구하기
for r in range(M):
    for c in range(N):
        if arr[r][c] == 0 and visited[r][c] == 0:
            area = 0
            # 큐에 넣고 방문처리
            queue.append((r, c))
            visited[r][c] = 1

            while queue:
                i, j = queue.popleft()
                # pop할 때마다 넓이 증가
                area += 1
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]

                    if ni < 0 or ni >= M or nj < 0 or nj >= N:
                        continue

                    if arr[ni][nj] == 0 and visited[ni][nj] == 0:
                        queue.append((ni, nj))
                        visited[ni][nj] = 1

            area_list.append(area)
            
print(len(area_list))
print(*sorted(area_list))



