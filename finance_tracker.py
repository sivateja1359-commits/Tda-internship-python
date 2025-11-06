import csv
import os
from datetime import datetime
from collections import defaultdict

FILE_NAME = "expenses.csv"
FIELDS = ["date", "category", "description", "amount"]

def init_file():
    """Create the file with headers if it doesn't already exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()

def add_expense():
    """Add a new expense entry."""
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    category = input("Enter category (Food, Rent, Transport, etc.): ")
    description = input("Enter a short description: ")
    amount = input("Enter amount: ")

    try:
        amount = float(amount)
    except ValueError:
        print("❌ Invalid amount. Try again.")
        return

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writerow({
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        })
    print("✅ Expense added successfully!")

def view_expenses():
    """Display all saved expenses."""
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)
            print("\n📌 All Expenses:")
            for row in reader:
                print(f"{row['date']} | {row['category']} | {row['description']} | ${row['amount']}")
    except FileNotFoundError:
        print("❌ No data file found. Add an expense first.")

def generate_monthly_report():
    """Generate and display a report grouped by month and category."""
    report = defaultdict(lambda: defaultdict(float))

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                month = row["date"][:7]  # YYYY-MM
                report[month][row["category"]] += float(row["amount"])
    except FileNotFoundError:
        print("❌ No data to report. Add expenses first.")
        return

    print("\n📊 Monthly Report:")
    for month, categories in report.items():
        print(f"\n--- {month} ---")
        for category, total in categories.items():
            print(f"{category}: ${total:.2f}")

def main():
    init_file()
    while True:
        print("\n==== PERSONAL FINANCE TRACKER ====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Generate Monthly Report")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            generate_monthly_report()
        elif choice == "4":
            print("👋 Exiting. Have a great day!")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()