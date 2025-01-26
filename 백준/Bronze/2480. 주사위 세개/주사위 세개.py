import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
dice = [0] * 7

for num in arr:
    dice[num] += 1

if max(dice) == 3:
    prize = 10000 + 1000 * dice.index(3)
elif max(dice) == 2:
    prize = 1000 + 100 * dice.index(2)
else:
    prize = 100 * max(arr)

print(prize)