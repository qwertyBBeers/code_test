a1 = input().split()
roll = [int(a1[0]), int(a1[1]), int(a1[2])]
pride = 0

if roll[1] == roll[2] and roll[2] == roll[0]:
    pride = 10000 + roll[0] * 1000
elif roll[0] == roll[1] or roll[1] == roll[2]:
    pride = 1000 + roll[1] * 100
elif roll[0] == roll[2]:
    pride = 1000 + roll[0] * 100
else:
    pride = max(roll) * 100

print(pride)