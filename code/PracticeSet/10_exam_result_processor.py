marks = list(map(int, input().split()))

failed = False
for mark in marks:
    if mark < 35:
        failed = True
        break

if failed:
    print("FAIL")
else:
    average = sum(marks) / len(marks)
    if average >= 75:
        print("DISTINCTION")
    else:
        print("PASS")
