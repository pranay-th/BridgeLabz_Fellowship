import random 

die=[]
max_rolls=5
count=0
while count < max_rolls:
    roll=random.randint(1,6)
    die.append(roll)
    count+=1
    if roll==6:
        print(f"Congratulations you won! Rolls: {die}")
        die.sort()
        break 
        count+=1
    elif count<max_rolls and roll!=6:
        print(f"Keep going! Rolls: {die}")
    else:
        print(f"Sorry! You ran out of rolls. Rolls: {die}")
        die.sort()
    
print(f"Sorted rolls: {die}")
