name = input("Enter the user name: ")
place1 = input("Enter the first place you would like to visit: ")
place2 = input("Enter the second place you would like to visit: ")
place3 = input("Enter the third place you would like to visit: ")
year = input("Enter the year to visit: ")

print(f"\nHello {name} and places to visit are ", end='')
print(place1, place2, place3, sep=', ', end=' ')
print(f"in the year {year}")
