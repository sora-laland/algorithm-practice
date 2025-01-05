import sys
input = sys.stdin.readline

st = []
K = int(input())
for _ in range(K):
    n = int(input())
    if n:
        st.append(n)
    else:
        st.pop()
print(sum(st))