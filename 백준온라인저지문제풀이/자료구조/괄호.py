a1 = int(input())
result = []

for i in range(0, a1):
    a2 = input()
    a3 = list(a2)
    checking_point = 0
    result1 = 0
    result2 = 0
    for j in range(0, len(a3)):
        if a3[j] == "(":
            result1 += 1
        elif a3[j] == ")":
            result2 += 1
        
        if result1 < result2:
            result.append("NO")
            checking_point = 1
            break
            
    if result1 == result2 and checking_point == 0:
        result.append("YES")
    elif result1 != result2 and checking_point == 0:
        result.append("NO")
    
for i in range(0, a1):
    print(result[i])
