import sys
input = sys.stdin.readline

N = int(input())
Ai = list(map(int, input().split()))
B, C = map(int, input().split())

# 각 시험장에서 필요한 감독관 수 구하기
def dir(x):
    cnt = 1
    cnt += max(0, x - B) // C
    if max(0, x - B) % C > 0:
        cnt += 1
    return cnt

result = list(map(dir, Ai))
print(sum(result))