import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()

# 산술평균
arithmetic_mean = round(sum(arr) / N)
print(arithmetic_mean)

# 중앙값
median = arr[N // 2]
print(median)
# 최빈값
# 빈 딕셔너리 생성
count_dict = {num: 0 for num in arr}
# 개수를 세서 밸류에 넣어줌
for num in arr:
    count_dict[num] += 1

modes = []
# 키와 밸류를 돌면서 최빈값들을 골라냄
for k, v in count_dict.items():
    if v == max(count_dict.values()):
        modes.append(k)

if len(modes) == 1:
    print(*modes)
else:
    print(modes[1])

# 범위
range_a = max(arr) - min(arr)
print(range_a)
