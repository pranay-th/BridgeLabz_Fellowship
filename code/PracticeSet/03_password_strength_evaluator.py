password = input()

has_digit = False
has_upper = False

for char in password:
    if char.isdigit():
        has_digit = True
    if char.isupper():
        has_upper = True

if has_digit and has_upper and len(password) >= 8:
    print("STRONG")
else:
    print("WEAK")
