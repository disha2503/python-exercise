minutes = input("Enter total minutes: ")
# 1min = 1/60hr
hours = int(minutes) / 60

remaining_minutes = int(minutes) % 60
print(f"Total time is {int(hours)} hours and {remaining_minutes} minutes")
