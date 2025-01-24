import sys
input = sys.stdin.readline

arr = list(range(1, 21))

def card(a, b):
    first = arr[:a-1]
    second = arr[a-1:b]
    third = arr[b:]
    return first + second[::-1] + third


for _ in range(10):
    a, b = map(int, input().split())
    arr = card(a, b)

print(*arr)