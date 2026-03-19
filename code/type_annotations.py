# PROG 4.2: Function Parameter Type Annotation

def calculate_final_score(total_sum: int, bonus_points: int) -> int:
  final_score = total_sum + bonus_points
  return final_score

total_sum = 10
bonus_points = 20

print(f"Data Type of total_sum is {type(total_sum)} and ")
print(f"bonus_points is {type(bonus_points)}")

final_score = calculate_final_score(total_sum, bonus_points)
print(f"Final Score is {final_score}")
