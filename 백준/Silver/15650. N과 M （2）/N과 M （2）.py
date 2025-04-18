import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(range(1, N+1))
path = []

def combi(x):

    if x == M:
        print(*path)
        return

    for num in arr:
        if num in path:
            continue
        if path and num < path[-1]:
            continue
        path.append(num)

        combi(x+1)
        path.pop()

combi(0)

