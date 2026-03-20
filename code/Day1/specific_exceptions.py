# 6.2 Handling Exact User Error

def calculate_final_score(total_sum: int, bonus_points: int) -> int:
  final_score = total_sum + bonus_points
  return final_score

try:
  total_sum = int(input("Enter value for Total Sum "))
  bonus_points = int(input("Enter value for Bonus Points "))
  
  print(f"Data Type of total_sum is {type(total_sum)} and ")
  print(f"bonus_points is {type(bonus_points)}")
  
  final_score = calculate_final_score(total_sum, bonus_points)
  print(f"Final Score is {final_score}")
except ValueError as e:
  print(f"ValueError: Invalid input. Please enter numeric values. Error: {e}")
except Exception as e:
  print(f"An unexpected error occurred: {e}")
