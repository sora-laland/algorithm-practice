import sys
input = sys.stdin.readline

N, X = map(int, input().split())
A = list(map(int, input().split()))

answer = list(filter(lambda x: x < X, A))
print(*answer)