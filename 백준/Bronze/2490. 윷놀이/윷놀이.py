import sys
input = sys.stdin.readline

yuts = { 3: "A", 2: "B", 1: "C", 0: "D", 4: "E"}

for _ in range(3):
    yut = list(map(int, input().split()))
    print(yuts[(sum(yut))])