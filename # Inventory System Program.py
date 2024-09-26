# Inventory System Program

# Initialize an empty dictionary to store the inventory
inventory = {}

def add_item(name, quantity):
    """
    Add a new item to the inventory or update the quantity of an existing item.
    """
    if name in inventory:
        # If the item already exists, update its quantity
        inventory[name] += quantity
    else:
        # If the item does not exist, add it to the inventory
        inventory[name] = quantity

def get_item_info(name):
    """
    Retrieve information about a specific item in the inventory.
    """
    if name in inventory:
        return f"Item: {name}, Quantity: {inventory[name]}"
    else:
        return f"Item {name} not found in the inventory."

def calculate_total_quantity():
    """
    Calculate and display the total quantity of all items in the inventory.
    """
    total_quantity = sum(inventory.values())
    return f"Total quantity of all items: {total_quantity}"

# Main program loop
while True:
    print("Inventory System Menu:")
    print("1. Add item to inventory")
    print("2. Get item information")
    print("3. Calculate total quantity")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input("Enter item name: ")
        quantity = int(input("Enter item quantity: "))
        add_item(name, quantity)
        print(f"Item {name} added to inventory with quantity {quantity}.")
    
    elif choice == "2":
        name = input("Enter item name: ")
        print(get_item_info(name))
    
    elif choice == "3":
        print(calculate_total_quantity())
    
    elif choice == "4":
        break
    
    else:
        print("Invalid choice. Please try again.")