def load_data():
    try:
        with open("data.txt", "r") as file:
            return eval(file.read())   # loads saved data as Python list
    except:
        return []   # return empty list if file does not exist


def save_data(data):
    with open("data.txt", "w") as file:
        file.write(str(data))


def add_expense(data):
    print("\n📌 Add New Expense")
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    note = input("Short note/description: ")

    data.append({"date": date, "category": category, "amount": amount, "note": note})
    save_data(data)
    print("✅ Expense Saved!\n")


def view_expenses(data):
    print("\n=== All Expenses ===")
    if not data:
        print("No expenses yet.\n")
        return

    for item in data:
        print(f"{item['date']} | {item['category']} | ${item['amount']} | {item['note']}")
    print()


def monthly_total(data):
    print("\n=== Monthly Spending Summary ===")
    if not data:
        print("No expenses yet.\n")
        return

    totals = {}
    for item in data:
        month = item['date'][:7]  # YYYY-MM
        totals[month] = totals.get(month, 0) + item['amount']

    for month, total in totals.items():
        print(f"{month}: ${total}")
    print()


def main():
    data = load_data()

    while True:
        print("====== PERSONAL FINANCE TRACKER ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            add_expense(data)
        elif choice == "2":
            view_expenses(data)
        elif choice == "3":
            monthly_total(data)
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.\n")


main()