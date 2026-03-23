number = int(input())

while number >= 10:
    digit_sum = 0
    temp = number
    while temp > 0:
        digit_sum += temp % 10
        temp = temp // 10
    number -= digit_sum

print(number)
