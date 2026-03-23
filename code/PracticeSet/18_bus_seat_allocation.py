n = int(input())

available_seats = 40

for _ in range(n):
    request = int(input())
    if available_seats >= request:
        available_seats -= request
        print("CONFIRMED")
    else:
        print("WAITLISTED")
