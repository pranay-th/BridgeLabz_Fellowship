PI = 22/7

radius_inch = float(input("Enter the radius of the circle in inches: "))

radius_cm = radius_inch * 2.54

circumference = 2 * PI * radius_cm
area = PI * (radius_cm ** 2)

print(f"\nCircumference of the Circle is {circumference:.2f} cm and Area of the Cricle is {area:.2f} sqcm")
