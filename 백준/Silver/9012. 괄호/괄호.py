import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    parenthesis = input().rstrip()
    st = []
    for each in parenthesis:
        if each == "(":
            st.append(each)
        else:
            if st and st[-1] == "(":
                st.pop()
            else:
                st.append(each)

    if st:
        print("NO")
    else:
        print("YES")