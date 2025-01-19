import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
st = []
NGE = [-1] * N

for i in range(N):
    while st and st[-1][1] < arr[i]:
        # st의 값과 비교해서 작으면 넣고 크면 pop
        # 감소스택이 되어야 함
        NGE[st.pop()[0]] = arr[i]
    st.append([i, arr[i]])

print(*NGE)