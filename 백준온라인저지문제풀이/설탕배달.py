a1=input()
a1 = int(a1)
result = 0

checking_point = 0
num5 = a1//5
7

for i in range (num5, -1, -1):
    if (a1-5*i)%3 == 0:
        result = i + (a1-5*i)//3
        print(result)
        checking_point = 1
        break
if checking_point == 0:
    print(-1)

