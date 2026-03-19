def add_nums(num1, num2):
  if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
    sum_result = num1 + num2
    return sum_result
  else:
    print("Both inputs must be numbers.")
    return None

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
result = add_nums(num1,num2)
print(result)
