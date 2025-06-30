import datetime

def print_day_of_week():
    today = datetime.date.today()
    print("Today's date:", today)
    print("Day of the week:", today.strftime("%A"))

def birthday_info():
    bday_str = input("\nEnter your birthday (YYYY-MM-DD): ")
    bday = datetime.datetime.strptime(bday_str, "%Y-%m-%d").date()
    today = datetime.date.today()

    age = today.year - bday.year
    if (today.month, today.day) < (bday.month, bday.day):
        age -= 1

    next_bday = datetime.date(today.year, bday.month, bday.day)
    if next_bday < today:
        next_bday = datetime.date(today.year + 1, bday.month, bday.day)

    now = datetime.datetime.now()
    next_bday_datetime = datetime.datetime.combine(next_bday, datetime.time())
    delta = next_bday_datetime - now

    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    seconds = delta.seconds % 60
   
    print(f"\nYou are {age} years old.")
    print(f"Time until your next birthday: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")

def compute_double_day(b1_str, b2_str):
    b1 = datetime.datetime.strptime(b1_str, "%Y-%m-%d")
    b2 = datetime.datetime.strptime(b2_str, "%Y-%m-%d")

    if b1 > b2:
        b1, b2 = b2, b1  
        

    delta = b2 - b1
    double_day = b2 + delta
    print(f"\nDouble Day (when one is twice as old as the other): {double_day.date()}")

def n_times_day(b1_str, b2_str, n):
    b1 = datetime.datetime.strptime(b1_str, "%Y-%m-%d")
    b2 = datetime.datetime.strptime(b2_str, "%Y-%m-%d")

    if b1 > b2:
        b1, b2 = b2, b1

    delta = b2 - b1
    n_day = b2 + delta / (n - 1)
    print(f"\nDay when one person is {n:.1f} times older than the other: {n_day.date()}")

if __name__ == "__main__":
    print("\n--- PART 1: Current Day of the Week ---")
    print_day_of_week()

    print("\n--- PART 2: Age and Next Birthday Info ---")
    birthday_info()

    print("\n--- PART 3: Double Day ---")
    b1 = input("Enter the first birth date (YYYY-MM-DD): ")
    b2 = input("Enter the second birth date (YYYY-MM-DD): ")
    compute_double_day(b1, b2)

    print("\n--- PART 4: N-Times Older Day ---")
    n = float(input("Enter the multiplier (e.g., 2 for twice as old): "))
    n_times_day(b1, b2, n)
