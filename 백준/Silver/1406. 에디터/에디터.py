import sys
input = sys.stdin.readline
from collections import deque

left_arr = deque(input().rstrip())
right_arr = deque()
M = int(input())

for _ in range(M):
    command, *word = input().split()

    if command == 'L':
        if len(left_arr) == 0:
            continue
        right_arr.appendleft(left_arr.pop())
        # print(left_arr, "|", right_arr)

    elif command == 'D':
        if len(right_arr) == 0:
            continue
        left_arr.append(right_arr.popleft())
        # print(left_arr, "|", right_arr)

    elif command == 'B':
        if len(left_arr) == 0:
            continue
        left_arr.pop()
        # print(left_arr, "|", right_arr)

    else:
        left_arr.append(word[0])
        # print(left_arr, "|", right_arr)


print("".join(left_arr), end="")
print("".join(right_arr))
