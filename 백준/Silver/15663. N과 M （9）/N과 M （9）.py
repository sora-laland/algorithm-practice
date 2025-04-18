import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [0] * N
path = []

# 순열
def perm(x):
    check = 0

    if x == M:
        print(*path)
        return


    for i in range(N):

        # 방문했던 곳이면 넘어감
        if visited[i]:
            continue
        # 같은 뎁스내에서 이전과 같은 값이면 넘어감
        if check == arr[i]:
            continue

        # 방문 표시
        path.append(arr[i])
        visited[i] = 1
        check = arr[i]

        perm(x+1)

        path.pop()
        visited[i] = 0

perm(0)
