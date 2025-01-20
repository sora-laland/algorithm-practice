import sys
input = sys.stdin.readline

while True:
    sentence = input().rstrip()
    if sentence == ".":
        break

    brackets = []
    for char in sentence:
        if char in "()[]":
            brackets.append(char)

    stack = []
    for bracket in brackets:

        if bracket in "([":
            stack.append(bracket)
        else:
            if bracket == "]" and stack and stack[-1] == "[":
                stack.pop()
            elif bracket == ")" and stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(bracket)

    if stack: print("no")
    else: print("yes")