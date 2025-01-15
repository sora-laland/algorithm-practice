import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
for _ in range(N):
    ks = input().rstrip()
    l_pass = deque()
    r_pass = deque()

    for char in ks:
        if char == '<':
            if len(l_pass) == 0:
                continue
            r_pass.appendleft(l_pass.pop())
        elif char == '>':
            if len(r_pass) == 0:
                continue
            l_pass.append(r_pass.popleft())
        elif char == '-':
            if len(l_pass) == 0:
                continue
            l_pass.pop()
        else:
            l_pass.append(char)

    print(''.join(l_pass)+''.join(r_pass))