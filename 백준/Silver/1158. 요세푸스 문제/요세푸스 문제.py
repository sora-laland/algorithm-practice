import sys
input = sys.stdin.readline

N, K = map(int, input().split())

arr = list(range(1, N+1))
flag = K - 1
result = []

while arr:
    result.append(str(arr.pop(flag)))
    flag += K - 1

    if len(arr) == 0:
        break

    while flag >= len(arr):
        flag -= len(arr)

print("<", end="")
print(", ".join(result), end="")
print(">")
