from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client['shop'] 
collection = db['products']

def save_items_to_db(items):
    for item_id, item in items.items():
        collection.update_one({'_id': item_id}, {'$set': item}, upsert=True)

def load_items_from_db():
    items = {}
    for item in collection.find():
        items[item['_id']] = {
            'Name': item['Name'],
            'Quantity': item['Quantity'],
            'Price': item['Price']
        }
    return items

def print_items(items):
    for item_id, item in items.items():
        print(f"ID: {item_id}, Name: {item['Name']}, Quantity: {item['Quantity']}, Price: {item['Price']}")

def add_product():
    name = input("Enter product name: ")
    quantity = int(input("Enter product quantity: "))
    price = float(input("Enter product price: "))
    
    items = load_items_from_db()
    new_id = max(items.keys()) + 1 if items else 1
    items[new_id] = {'Name': name, 'Quantity': quantity, 'Price': price}
    
    save_items_to_db(items)
    print("Product added successfully.")

def add_product_from_csv():
    file_name = input("Enter the CSV file name (with extension): ")
    
    if not os.path.exists(file_name):
        print("File not found.")
        return
    
    csv_items = load_items_from_csv(file_name)  
    db_items = load_items_from_db()  
    
    max_id = max(db_items.keys()) if db_items else 0
    for item_id, item in csv_items.items():
        db_items[max_id + item_id + 1] = item
    
    save_items_to_db(db_items)
    print("Products added successfully.")
def delete_product():
    product_id = int(input("Enter the ID of the product you want to delete: "))
    items = load_items_from_db()
    if product_id in items:
        collection.delete_one({'_id': product_id})
        print("Product deleted successfully.")
    else:
        print("Invalid product ID.")

def display_products():
    items = load_items_from_db()
    if items:
        print("Available products:")
        print_items(items)
    else:
        print("No products available.")

def purchase_product():
    product_id = int(input("Enter the ID of the product you want to purchase: "))
    items = load_items_from_db()
    
    if product_id in items:
        quantity_available = items[product_id]['Quantity']
        if quantity_available > 0:
            quantity_to_buy = int(input("Enter the quantity you want to purchase: "))
            if quantity_to_buy <= quantity_available:
                items[product_id]['Quantity'] -= quantity_to_buy
                save_items_to_db(items)
                total_price = items[product_id]['Price'] * quantity_to_buy
                print(f"Thank you for your purchase! Total price: {total_price}")
                return quantity_to_buy  # Return the quantity purchased
            else:
                print("Insufficient quantity available.")
        else:
            print("Sorry, the product is out of stock.")
    else:
        print("Invalid product ID.")
    return 0  
def shopkeeper():
    password = "password123" 
    pass_attempt = input("Enter password: ")
    
    if pass_attempt == password:
        print("Access granted.")
        while True:
            print("1. Display Products\n2. Add Manually\n3. Add From CSV\n4. Delete Product\n5. Exit")
            choice = input("Enter your choice: ")
            if choice == '5':
                print("Exiting shopkeeper mode.")
                break
            elif choice == '1':
                display_products()
            elif choice == '2':
                add_product()
            elif choice == '3':
                add_product_from_csv()
            elif choice == '4':
                delete_product()
            else:
                print("Invalid choice.")
    else:
        print("Incorrect password. Access denied.")

def customer():
    total_products_purchased = 0  
    while True:
        print("1. Display Products\n2. Purchase Product\n3. Exit")
        choice = input("Please select an option: ")
        if choice == '3':
            print("Exiting customer mode.")
            break
        elif choice == '1':
            display_products()
        elif choice == '2':
            while True:
                purchased_quantity = purchase_product()
                total_products_purchased += purchased_quantity 
                choice = input("Do you want to purchase another product? (yes/no): ")
                if choice.lower() != 'yes':
                    break
        else:
            print("Invalid choice.")
    
    print(f"Total products purchased in last transaction: {total_products_purchased}")

def main():
    if collection.count_documents({}) == 0:
        default_items = {
            1: {'Name': 'Apple', 'Quantity': 10, 'Price': 145},
            2: {'Name': 'Banana', 'Quantity': 20, 'Price': 33},
            3: {'Name': 'Orange', 'Quantity': 15, 'Price': 23}
        }
        save_items_to_db(default_items)
    
    while True:
        user_type = int(input("Are you a shopkeeper or a customer? Enter '1.shopkeeper' or '2.customer' (Enter '3.exit' to quit):"))
        if user_type == 1:
            shopkeeper()
        elif user_type == 2:
            customer()
        elif user_type == 3:
            print("Exiting the program...")
            break
        else:
            print("Invalid input. Please enter either 'shopkeeper' or 'customer'.")

if __name__ == "__main__":
    main()
