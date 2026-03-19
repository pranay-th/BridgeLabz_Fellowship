# PROG 5.1: Hard Coding Values

PI = 3.14

def calculate_circle_area(radius: float) -> float:
  area = PI * radius * radius
  return area

radius = 2
area = calculate_circle_area(radius)
print(f"Area of a Circle with radius = {radius} is {area}")
