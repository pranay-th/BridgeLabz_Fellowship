n = int(input())
inflows = list(map(int, input().split()))

tank = 0
overflow_minute = 0

for i in range(n):
    tank += inflows[i]
    if tank > 1000:
        overflow_minute = i + 1
        break

print(overflow_minute)
