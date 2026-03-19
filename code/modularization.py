# PROG 3: Define Function

def calculate_final_score(total_sum: int, bonus_points: int) -> int:
  final_score = total_sum + bonus_points
  return final_score

total_sum = 10
bonus_points = 20
z = calculate_final_score(total_sum, bonus_points)

print(f"The value z is {z}")
print(f"Final Score is {z}")
