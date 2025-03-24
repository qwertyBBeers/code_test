a1 = int(input())
a2 = int(input())
result = 0

for i in range(a2):
    b1 = input().split()
    result += int(b1[0])*int(b1[1])
    
if a1 == result:
    print("Yes")
else:
    print("No")