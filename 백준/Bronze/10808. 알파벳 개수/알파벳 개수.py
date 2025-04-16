import sys
input = sys.stdin.readline

S = input()
alphabet_str = 'abcdefghijklmnopqrstuvwxyz'


for item in alphabet_str:
    print(S.count(item), end=" ")