import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
st = []
result = [0] * N

for i in range(N-1, -1, -1):
    while st and arr[i] > st[-1][1]:
        result[st.pop()[0]] = i + 1
    st.append([i, arr[i]])

print(*result)