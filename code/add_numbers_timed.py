# PROG 1.2: Adding 2 Numbers Measuring Time
import time

def add_nums(num1: int, num2: int) -> int:
  if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
    sum_result = num1 + num2
    return sum_result
  else:
    print("Both inputs must be numbers.")
    return None

start_time = time.time()
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = add_nums(num1, num2)
end_time = time.time()

print(f"The sum of {num1} and {num2} is {result}")
print(f"Time taken: {end_time - start_time:.6f} seconds")
