import sys
input = sys.stdin.readline

a, b = map(int, input().split())
A, B = min(a, b), max(a, b)

if A == B:
    print(0)
else:
    print(B-A-1)
for i in range(A+1, B):
    print(i, end=" ")