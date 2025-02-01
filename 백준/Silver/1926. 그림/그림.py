import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
visited = [[0] * m for _ in range(n)]
queue = deque()
max_area = 0
cnt = 0

# bfs
for r in range(n):
    for c in range(m):
        if arr[r][c] == 1 and visited[r][c] == 0:
            # 첫번째 원소 넣고 방문 처리
            queue.append((r, c))
            visited[r][c] = 1
            cnt += 1
            area = 0
            while queue:
                i, j = queue.popleft()
                area += 1
                # 상하좌우 돌면서 방문 안했고 1이면 넣어, 방문처리
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]

                    # 범위를 벗어나면
                    if ni < 0 or ni >= n or nj < 0 or nj >= m:
                        continue
                    # 0이면
                    if arr[ni][nj] == 0:
                        continue
                    # 방문했으면
                    if visited[ni][nj] == 1:
                        continue

                    queue.append((ni, nj))
                    visited[ni][nj] = 1

            max_area = max(max_area, area)

print(cnt)
print(max_area)