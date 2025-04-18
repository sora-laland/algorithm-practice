import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
path = []

# 조합
def repeated_combi(x):

    if x == M:
        print(*path)
        return

    for num in arr:
        # 직전에 뽑은 요소가 지금보다 크면 넘겨
        # 중복이 허용되므로 같아도 됨
        if path and num < path[-1]:
            continue

        path.append(num)
        repeated_combi(x+1)
        path.pop()

repeated_combi(0)

