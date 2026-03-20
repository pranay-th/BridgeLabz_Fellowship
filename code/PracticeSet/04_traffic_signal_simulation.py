t = int(input())

t = t % 90
if t == 0:
    t = 90

if 1 <= t <= 30:
    print("RED")
elif 31 <= t <= 45:
    print("YELLOW")
else:
    print("GREEN")
