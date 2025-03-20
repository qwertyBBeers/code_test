a = []
for i in range(2):
    a.append(int(input()))

if a[0] > 0 and a[1] > 0:
    print(1)
elif a[0] < 0 and a[1] > 0:
    print(2)
elif a[0] < 0 and a[1] < 0:
    print(3)
else:
    print(4)
    