import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
path = []

# 중복순열
def repeated_perm(x):

    if x == M:
        print(*path)
        return

    for num in arr:
        path.append(num)
        repeated_perm(x+1)
        path.pop()

repeated_perm(0)
