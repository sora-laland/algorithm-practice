import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.reverse()

cnt = 0
idx = 0
while K:
    coin = arr[idx]
    now = K // coin
    if now > 0:
        cnt += now
        K = K - now * coin
    idx += 1
print(cnt)