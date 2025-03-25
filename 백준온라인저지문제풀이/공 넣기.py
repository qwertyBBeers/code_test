a1 = list(map(int, input().split()))
result = [0]*a1[0]

for i in range(a1[1]):
    a2 = list(map(int, input().split()))
    for j in range(a2[0]-1, a2[1], 1):
        result[j] = a2[2]

for i in range(a1[0]):
    print(result[i], end=" ")        
        