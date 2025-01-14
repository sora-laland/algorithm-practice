import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

Y = sum(list(map(lambda x:(x//30+1)*10, arr)))
M = sum(list(map(lambda x:(x//60+1)*15, arr)))

if Y < M:
    print("Y", Y)
elif Y > M:
    print("M", M)
else:
    print("Y M", Y)
