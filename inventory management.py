import pandas as pd

# Load or create data files
def load_data():
    try:
        products = pd.read_csv("products.csv", dtype={"ProductID": str})
    except FileNotFoundError:
        products = pd.DataFrame(columns=["ProductID", "Name", "Price", "Quantity"])
        products.to_csv("products.csv", index=False)

    try:
        sales = pd.read_csv("sales.csv", dtype={"ProductID": str, "SaleID": int})
    except FileNotFoundError:
        sales = pd.DataFrame(columns=["SaleID", "ProductID", "QuantitySold", "TotalPrice"])
        sales.to_csv("sales.csv", index=False)

    return products, sales


def save_data(products, sales):
    products.to_csv("products.csv", index=False)
    sales.to_csv("sales.csv", index=False)


# Add a new product
def add_product(products):
    pid = input("Enter Product ID: ").strip()
    name = input("Enter Product Name: ")

    # Validate price
    while True:
        try:
            price = float(input("Enter Product Price: "))
            break
        except ValueError:
            print("Invalid price! Enter numbers only.")

    # Validate quantity
    while True:
        try:
            quantity = int(input("Enter Product Quantity: "))
            break
        except ValueError:
            print("Invalid quantity! Enter whole numbers only.")

    new_product = {"ProductID": pid, "Name": name, "Price": price, "Quantity": quantity}

    products = pd.concat([products, pd.DataFrame([new_product])], ignore_index=True)
    print("Product added successfully!\n")

    return products


# Update stock quantity
def update_stock(products):
    pid = input("Enter Product ID to update: ").strip()

    if pid not in products["ProductID"].values:
        print("Product not found.\n")
        return products

    while True:
        try:
            new_qty = int(input("Enter new stock quantity: "))
            break
        except ValueError:
            print("Invalid quantity! Enter whole numbers only.")

    products.loc[products["ProductID"] == pid, "Quantity"] = new_qty
    print("Stock updated!\n")

    return products


# Record a sale
def record_sale(products, sales):
    pid = input("Enter Product ID sold: ").strip()

    if pid not in products["ProductID"].values:
        print("Product not found.\n")
        return sales, products

    while True:
        try:
            quantity_sold = int(input("Enter quantity sold: "))
            break
        except ValueError:
            print("Invalid quantity! Numbers only.")

    product_row = products.loc[products["ProductID"] == pid]
    available = int(product_row["Quantity"].values[0])

    if quantity_sold > available:
        print("Not enough stock!\n")
        return sales, products

    price = float(product_row["Price"].values[0])
    total_price = price * quantity_sold

    products.loc[products["ProductID"] == pid, "Quantity"] = available - quantity_sold

    # Safe SaleID generation
    sale_id = (sales["SaleID"].max() + 1) if not sales.empty else 1

    new_sale = {
        "SaleID": sale_id,
        "ProductID": pid,
        "QuantitySold": quantity_sold,
        "TotalPrice": total_price
    }

    sales = pd.concat([sales, pd.DataFrame([new_sale])], ignore_index=True)
    print("Sale recorded!\n")

    return sales, products


# Generate reports
def generate_report(products, sales):
    print("\n----- INVENTORY REPORT -----")
    print(products)

    print("\n----- SALES REPORT -----")
    print(sales)

    print("\n----- TOTAL SALES -----")
    print("Total Revenue:", sales["TotalPrice"].sum(), "\n")


# Main menu loop
def main():
    products, sales = load_data()

    while True:
        print("""
===================================
   Inventory Management System
===================================
1. Add Product
2. Update Stock
3. Record Sale
4. Show Reports
5. Exit
""")

        choice = input("Enter choice: ")

        if choice == "1":
            products = add_product(products)
        elif choice == "2":
            products = update_stock(products)
        elif choice == "3":
            sales, products = record_sale(products, sales)
        elif choice == "4":
            generate_report(products, sales)
        elif choice == "5":
            save_data(products, sales)
            print("Data saved. Exiting program.")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
    