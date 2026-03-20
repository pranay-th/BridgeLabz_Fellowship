units = int(input())

bill = 0
if units <= 100:
    bill = units * 3
elif units <= 200:
    bill = 100 * 3 + (units - 100) * 5
else:
    bill = 100 * 3 + 100 * 5 + (units - 200) * 8

if units > 300:
    bill = bill * 1.1

print(int(bill))
