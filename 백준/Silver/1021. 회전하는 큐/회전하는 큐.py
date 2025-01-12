import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
deq = deque(range(1, N+1))
for item in arr:
    idx = deq.index(item)

    if idx != 0:
        if idx <= len(deq) // 2:
            deq.rotate(-idx)
            cnt += idx
        else:
            deq.rotate(len(deq) - idx)
            cnt += (len(deq) - idx)

    # 위에서 item의 index를 0으로 만들어놓음
    deq.popleft()

print(cnt)
