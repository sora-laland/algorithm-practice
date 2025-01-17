import sys
input = sys.stdin.readline

N = int(input())
height = [int(input()) for _ in range(N)]

stack = []
result = 0

for i in height:
    # i 건물을 못보는 건 stack에서 빼준다
    while stack and stack[-1] <= i:
        stack.pop()
    stack.append(i)
    result += len(stack)-1

print(result)