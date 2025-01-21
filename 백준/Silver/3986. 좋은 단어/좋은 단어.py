import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
for _ in range(N):
    word = input().rstrip()
    st = []
    for char in word:
        if st and st[-1] == char:
            st.pop()
        else:
            st.append(char)

    if len(st) == 0:
        cnt += 1

print(cnt)