# PROG 5.3 Handling Type Conversion

def calculate_final_score(total_sum: int, bonus_points: int) -> int:
  final_score = total_sum + bonus_points
  return final_score

total_sum = int(input("Enter value for Total Sum "))
bonus_points = int(input("Enter value for Bonus Points "))

print(f"Data Type of total_sum is {type(total_sum)} and ")
print(f"bonus_points is {type(bonus_points)}")

final_score = calculate_final_score(total_sum, bonus_points)
print(f"Final Score is {final_score}")
