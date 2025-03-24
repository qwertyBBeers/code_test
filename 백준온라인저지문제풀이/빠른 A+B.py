import sys

a1 = int(sys.stdin.readline())

for i in range(a1):
    a2 = sys.stdin.readline().rstrip().split()
    result = int(a2[0]) + int(a2[1])
    print(result)
