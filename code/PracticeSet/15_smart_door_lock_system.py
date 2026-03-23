correct_pin = input()

granted = False
for _ in range(3):
    attempt = input()
    if attempt == correct_pin:
        granted = True
        break

if granted:
    print("ACCESS GRANTED")
else:
    print("LOCKED")
