def groceries():
    print("You selected Groceries.")
    grocery_items = {
        1: {"name": "Rice", "quantity": 10, "price": 10, "per": "/kg"},
        2: {"name": "Bread", "quantity": 20, "price": 50, "per": "/pack"},
        3: {"name": "Milk", "quantity": 15, "price": 25, "per": "/pack"},
        4: {"name": "Eggs", "quantity": 30, "price": 3.99, "per": "/pack"},
        5: {"name": "Salt", "quantity": 25, "price": 40, "per": "/pack"}
    }
    print("Available groceries:")
    for num, details in grocery_items.items():
        print(f"{num}. {details['name']}: Quantity - {details['quantity']}, Price - ${details['price']:.2f}{details['per']}")

def soft_drinks():
    print("You selected Soft Drinks.")
    soft_drinks_items = {
        1: {"name": "Cola", "quantity": 20, "price": 22, "per": "/bottle"},
        2: {"name": "Sprite", "quantity": 15, "price": 22, "per": "/bottle"},
        3: {"name": "Fanta", "quantity": 15, "price": 22, "per": "/bottle"},
        4: {"name": "Pepsi", "quantity": 20, "price": 22, "per": "/bottle"},
        5: {"name": "Mountain Dew", "quantity": 10, "price": 22, "per": "/bottle"}
    }
    print("Available soft drinks:")
    for num, details in soft_drinks_items.items():
        print(f"{num}. {details['name']}: Quantity - {details['quantity']}, Price - ${details['price']:.2f} per pack")

def snacks():
    print("You selected Snacks.")
    snacks_items = {
        1: {"name": "Chips", "quantity": 20, "price": 20, "per": "/pack"},
        2: {"name": "Popcorn", "quantity": 15, "price": 49, "per": "/pack"},
        3: {"name": "Pretzels", "quantity": 10, "price": 79, "per": "/pack"},
        4: {"name": "Nuts", "quantity": 25, "price": 329, "per": "/pack"},
        5: {"name": "Crackers", "quantity": 20, "price": 69, "per": "/pack"}
    }
    print("Available snacks:")
    for num, details in snacks_items.items():
        print(f"{num}. {details['name']}: Quantity - {details['quantity']}, Price - ${details['price']:.2f}{details['per']}")

def fruits():
    print("You selected Fruits.")
    fruits_items = {
        1: {"name": "Apple", "quantity": 30, "price": 120, "per": "/kg"},
        2: {"name": "Banana", "quantity": 40, "price": 49, "per": "/kg"},
        3: {"name": "Orange", "quantity": 25, "price": 69, "per": "/kg"},
        4: {"name": "Grapes", "quantity": 20, "price": 79, "per": "/kg"},
        5: {"name": "Watermelon", "quantity": 5, "price": 29, "per": "/each"}
    }
    print("Available fruits:")
    for num, details in fruits_items.items():
        print(f"{num}. {details['name']}: Quantity - {details['quantity']}, Price - ${details['price']:.2f}{details['per']}")

def shopkeeper(choice):
    # Define the correct passcode
    correct_passcode = "password123"
    
    # Prompt the shopkeeper for the passcode
    passcode_attempt = input("Enter passcode: ")
    
    # Check if the passcode is correct
    if passcode_attempt == correct_passcode:
        switch = {
            1: groceries,
            2: soft_drinks,
            3: snacks,
            4: fruits
        }
        # Get the function corresponding to the choice, or None if choice is invalid
        selected_func = switch.get(choice)
        if selected_func:
            selected_func()
        else:
            print("Invalid choice. Please select a valid option.")
    else:
        print("Incorrect passcode. Access denied.")

choice = int(input("Enter your choice (1.Groceries 2.Soft Drinks 3.Snacks 4.Fruits): "))
shopkeeper(choice)