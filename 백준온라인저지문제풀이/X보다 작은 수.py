a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
a3 = 0
result = 0

for i in range(a1[0]):
    if a1[1] > a2[i]:
        print(a2[i], end=" ")