import csv
from datetime import datetime

FILENAME = "fitness_data.csv"

def add_entry():
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    workout_type = input("Workout Type (e.g. Running, Cycling, Yoga): ")
    duration = input("Duration or Calories burned: ")
    steps = input("Steps (optional): ")
    weight = input("Weight (optional): ")

    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, workout_type, duration, steps, weight])
    print("✅ Entry added successfully!")

def view_entries():
    try:
        with open(FILENAME, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("❌ No data found. Please add some entries first.")

def show_menu():
    while True:
        print("\n====== PERSONAL FITNESS TRACKER ======")
        print("1. Add New Entry")
        print("2. View All Entries")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_entry()
        elif choice == '2':
            view_entries()
        elif choice == '3':
            print("👋 Exiting. Stay healthy!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    show_menu()
