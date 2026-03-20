SCHOOL = "New School Of Learning"
CLASS = "Class XI"
SUBJECT_MARKS = 50
TOTAL_MARKS = 150
NUM_STUDENTS = 3

student1 = input("Enter name of student 1: ")
phy1 = int(input("Enter Physics marks out of 50 for student 1: "))
chem1 = int(input("Enter Chemistry marks out of 50 for student 1: "))
math1 = int(input("Enter Mathematics marks out of 50 for student 1: "))

total1 = phy1 + chem1 + math1

phy1_pct = (phy1 / SUBJECT_MARKS) * 100
chem1_pct = (chem1 / SUBJECT_MARKS) * 100
math1_pct = (math1 / SUBJECT_MARKS) * 100
total1_pct = (total1 / TOTAL_MARKS) * 100

print(f"\n{SCHOOL} - {CLASS} - {student1}")
print("-" * 72)
print("|     Subject     |   Total Marks   | Marks Obtained  |   Percentage    |")
print("-" * 72)
print(f"|     Physics     |       {SUBJECT_MARKS}        |       {phy1}        |      {phy1_pct}       |")
print(f"|    Chemistry    |       {SUBJECT_MARKS}        |       {chem1}        |      {chem1_pct}       |")
print(f"|   Mathematics   |       {SUBJECT_MARKS}        |       {math1}        |      {math1_pct}       |")
print("-" * 72)
print(f"|      Total      |       {TOTAL_MARKS}       |       {total1}       |      {total1_pct:.2f}      |")
print("-" * 72)

print("\n")
student2 = input("Enter name of student 2: ")
phy2 = int(input("Enter Physics marks out of 50 for student 2: "))
chem2 = int(input("Enter Chemistry marks out of 50 for student 2: "))
math2 = int(input("Enter Mathematics marks out of 50 for student 2: "))

total2 = phy2 + chem2 + math2

phy2_pct = (phy2 / SUBJECT_MARKS) * 100
chem2_pct = (chem2 / SUBJECT_MARKS) * 100
math2_pct = (math2 / SUBJECT_MARKS) * 100
total2_pct = (total2 / TOTAL_MARKS) * 100

print(f"\n{SCHOOL} - {CLASS} - {student2}")
print("-" * 72)
print("|     Subject     |   Total Marks   | Marks Obtained  |   Percentage    |")
print("-" * 72)
print(f"|     Physics     |       {SUBJECT_MARKS}        |       {phy2}        |      {phy2_pct}       |")
print(f"|    Chemistry    |       {SUBJECT_MARKS}        |       {chem2}        |      {chem2_pct}       |")
print(f"|   Mathematics   |       {SUBJECT_MARKS}        |       {math2}        |      {math2_pct}       |")
print("-" * 72)
print(f"|      Total      |       {TOTAL_MARKS}       |       {total2}       |      {total2_pct:.2f}      |")
print("-" * 72)

print("\n")
student3 = input("Enter name of student 3: ")
phy3 = int(input("Enter Physics marks out of 50 for student 3: "))
chem3 = int(input("Enter Chemistry marks out of 50 for student 3: "))
math3 = int(input("Enter Mathematics marks out of 50 for student 3: "))

total3 = phy3 + chem3 + math3

phy3_pct = (phy3 / SUBJECT_MARKS) * 100
chem3_pct = (chem3 / SUBJECT_MARKS) * 100
math3_pct = (math3 / SUBJECT_MARKS) * 100
total3_pct = (total3 / TOTAL_MARKS) * 100

print(f"\n{SCHOOL} - {CLASS} - {student3}")
print("-" * 72)
print("|     Subject     |   Total Marks   | Marks Obtained  |   Percentage    |")
print("-" * 72)
print(f"|     Physics     |       {SUBJECT_MARKS}        |       {phy3}        |      {phy3_pct}       |")
print(f"|    Chemistry    |       {SUBJECT_MARKS}        |       {chem3}        |      {chem3_pct}       |")
print(f"|   Mathematics   |       {SUBJECT_MARKS}        |       {math3}        |      {math3_pct}       |")
print("-" * 72)
print(f"|      Total      |       {TOTAL_MARKS}       |       {total3}       |      {total3_pct:.2f}      |")
print("-" * 72)

total_phy = phy1 + phy2 + phy3
total_chem = chem1 + chem2 + chem3
total_math = math1 + math2 + math3

avg_phy = total_phy / NUM_STUDENTS
avg_chem = total_chem / NUM_STUDENTS
avg_math = total_math / NUM_STUDENTS

avg_phy_pct = (avg_phy / SUBJECT_MARKS) * 100
avg_chem_pct = (avg_chem / SUBJECT_MARKS) * 100
avg_math_pct = (avg_math / SUBJECT_MARKS) * 100

total_all = total1 + total2 + total3
overall_pct = (total_all / (TOTAL_MARKS * NUM_STUDENTS)) * 100

print("\n\n")
print("Class Average And Percentage for Each Subject:")
print(f"Physics Average is {avg_phy:.2f} and Percentage is {avg_phy_pct:.2f}%")
print(f"Chemistry Average is {avg_chem:.2f} and Percentage is {avg_chem_pct:.2f}%")
print(f"Mathematics Average is {avg_math:.2f} and Percentage is {avg_math_pct:.2f}%")
print(f"Overall Percentage: {overall_pct:.2f}%")
