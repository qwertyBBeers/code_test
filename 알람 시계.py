a = input().split()
times = [int(a[0]), int(a[1])]
times[1] = times[1]-45
if times[1] < 0:
    times[1] += 60
    times[0] -= 1

if times[0] < 0:
    times[0] += 24

print(times[0],times[1])