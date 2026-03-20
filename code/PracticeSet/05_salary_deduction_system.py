salary = int(input())
late_days = int(input())
absent_days = int(input())

if late_days > 10:
    salary = salary * 0.9
elif late_days > 5:
    salary = salary * 0.95

if absent_days > 2:
    salary = salary * 0.95

print(int(salary))
