amount = int(input())

if amount >= 5000:
    amount = amount * 0.8
elif amount >= 3000:
    amount = amount * 0.9
elif amount >= 1000:
    amount = amount * 0.95

print(int(amount))
