balance = int(input())
n = int(input())

for _ in range(n):
    amount = int(input())
    if amount % 100 == 0 and balance >= amount:
        balance -= amount
        print("SUCCESS")
    else:
        print("FAILED")

print(balance)
