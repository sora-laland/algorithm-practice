import sys
input = sys.stdin.readline

dic = {}
N, M = map(int, input().split())

for _ in range(N):
    site, pw = input().split()
    dic[site] = pw

for _ in range(M):
    print(dic[input().strip()])