a1 = input().split()
a2 = input()

times = [int(a1[0]), int(a1[1]), int(a2)]

times[1] = times[1] + times[2]
while times[1] >= 60:
    if times[1] >= 60:
        times[1] -= 60
        times[0] +=1
        
    if times[0] >= 24:
        times[0] -= 24
    
print(times[0],times[1])