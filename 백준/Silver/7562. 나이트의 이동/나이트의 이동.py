import sys
from collections import deque
input = sys.stdin.readline

# 나이트가 갈 수 있는 곳
di = [-2, -1, 1, 2, 2, 1, -1, -2]
dj = [-1, -2, -2, -1, 1, 2, 2, 1]
N = int(input())
for _ in range(N):
    l = int(input())
    n1, n2 = map(int, input().split())
    t1, t2 = map(int, input().split())
    queue = deque()
    visited = [[0]*l for _ in range(l)]

    queue.append((n1, n2))
    visited[n1][n2] = 1

    while queue:
        if visited[t1][t2] > 0:
            break
        i, j = queue.popleft()
        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or ni >= l or nj < 0 or nj >= l:
                continue
            if visited[ni][nj] == 0:
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    print(visited[t1][t2] - 1)