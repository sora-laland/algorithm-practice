import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
path = []

# 조합
def combi(x):

    if x == M:
        print(*path)
        return

    for num in arr:
        # 직전에 뽑은 요소가 지금보다 크거나 같다면 넘겨
        if path and num <= path[-1]:
            continue
            
        path.append(num)
        combi(x+1)
        path.pop()

combi(0)