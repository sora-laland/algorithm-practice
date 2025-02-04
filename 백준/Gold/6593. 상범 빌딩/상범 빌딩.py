import sys
from collections import deque
input = sys.stdin.readline

di = [0, 0, 1, -1, 0, 0]
dj = [-1, 1, 0, 0, 0, 0]
df = [0, 0, 0, 0, 1, -1]

while True:
    L, R, C = map(int, input().split())

    if L == R == C == 0:
        break

    graph = []
    for _ in range(L):
        floor = []
        for _ in range(R+1):
            each = input().rstrip()
            if each == "":
                continue
            floor.append(each)
        graph.append(floor)


    queue = deque()
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]
    answer = 0

    for f in range(L):
        for i in range(R):
            for j in range(C):
                if graph[f][i][j] == "S":
                    queue.append((f, i, j))
                    visited[f][i][j] = 1
                    break

    while queue:
        f, i, j = queue.popleft()
        for k in range(6):
            nf = f + df[k]
            ni = i + di[k]
            nj = j + dj[k]
            # 빌딩 범위를 벗어나면 안됨
            if nf<0 or nf>=L or ni<0 or ni>=R or nj<0 or nj>= C:
                continue
            if graph[nf][ni][nj] == "." and visited[nf][ni][nj] == 0:
                queue.append((nf, ni, nj))
                visited[nf][ni][nj] = visited[f][i][j] + 1
            if graph[nf][ni][nj] == "E":
                answer = visited[f][i][j]
                break

    if answer:
        print(f'Escaped in {answer} minute(s).')
    else:
        print("Trapped!")
