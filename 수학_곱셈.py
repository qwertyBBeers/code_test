number1 = input()
number2 = input()
num1 = int(number1)
num2 = int(number2)
length = len(number2)
stack = 0
value = 0
ten = 0

a = [0] * length

temp = num2
for i in range(length):
    stack = temp % 10      
    temp //= 10            
    a[i] = stack

for i in range(length):
    ten = num1 * a[i]
    print(ten)
    ten = ten * (10 ** i)
    value += ten

print(value)