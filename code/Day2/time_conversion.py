seconds = int(input("Enter the time duration in seconds: "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
secs = seconds % 60

print(f"\nTime duration of {seconds} seconds in HH:MM:SS format is {hours:02d}:{minutes:02d}:{secs:02d}")
