import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
path = []

# 순열
def perm(x):

    if x == M:
        print(*path)
        return

    for num in arr:
        if num in path:
            continue
        path.append(num)

        perm(x+1)
        path.pop()

perm(0)