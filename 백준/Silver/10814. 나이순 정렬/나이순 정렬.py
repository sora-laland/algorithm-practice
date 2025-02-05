import sys
input = sys.stdin.readline

arr = []
N = int(input())
for i in range(N):
    age_name = input().split()
    age_name.append(i)
    arr.append(age_name)

arr.sort(key=lambda x:(int(x[0]), x[2]))

for i in range(N):
    print(*arr[i][:2])