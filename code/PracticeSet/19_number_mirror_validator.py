number = int(input())

original = number
reversed_num = 0

while number > 0:
    digit = number % 10
    reversed_num = reversed_num * 10 + digit
    number = number // 10

if original == reversed_num:
    print("PALINDROME")
else:
    print("NOT PALINDROME")
