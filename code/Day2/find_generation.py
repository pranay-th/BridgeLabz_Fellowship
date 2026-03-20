year = int(input("Enter Birth Year: "))

print(f"\nBirth Year is {year}")
print(f"Is Baby Boomer: {True if 1946 <= year <= 1964 else False}")
print(f"Is Gen X: {True if 1965 <= year <= 1980 else False}")
print(f"Is Millennial: {True if 1981 <= year <= 1996 else False}")
print(f"Is Gen Z: {True if 1997 <= year <= 2012 else False}")
print(f"Is Gen Alpha: {True if 2013 <= year <= 2025 else False}")
