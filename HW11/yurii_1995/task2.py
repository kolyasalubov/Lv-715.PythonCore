# home work 11, task 2

days_of_week = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

try:
    given_number = int(input("Enter the number the day of week corresponds to: "))

    for key in days_of_week.keys():
        if key == given_number:
            print(f"The given number {given_number} is equil to {days_of_week[key]}")
        else:
            raise KeyError("Your number is not equil to any of days of week (1-7)")
except KeyError as e:
    print(e)
except ValueError as e:
    print("You have typed the incorrect data!")
