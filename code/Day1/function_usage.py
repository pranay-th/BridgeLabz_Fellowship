# PROG 4.1 Proper Function Usage

def calculate_final_score(total_sum: int, bonus_points: int) -> int:
  final_score = total_sum + bonus_points
  return final_score

total_sum = 10
bonus_points = 20
final_score = calculate_final_score(total_sum, bonus_points)
print(f"Final Score is {final_score}")
