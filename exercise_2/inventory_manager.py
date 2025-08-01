#  Smart Inventory Manager


import sys
import datetime

# Initialize the inventory dictionary
# Each item is a key with a value being a dictionary of its details
inventory = {}

def add_item(inventory, item_name, price, stock, category):
    """
    Adds a new item to the inventory.
    Checks if the item already exists to prevent duplicates.
    """
    if item_name in inventory:
        print(f"Error: Item '{item_name}' already exists.")
        return
    # Add the new item with provided details
    inventory[item_name] = {
        'price': price,
        'stock': stock,
        'category': category,
        'last_updated': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Record timestamp
    }
    print(f"\nItem '{item_name}' added successfully.")
    
    
def list_inventory(inventory):
        """Lists the inventory with item numbers."""
        if not inventory:
          print("Inventory is empty.")
          return

        print("Inventory Items:")
        for idx, (item_name, item_details) in enumerate(inventory.items(), start=1):
         print(f"{idx}. {item_name}:")
         print(f"   Price: ${item_details['price']:.2f}")
         print(f"   Stock: {item_details['stock']}")
         print(f"   Category: {item_details['category']}")
         print(f"   Last Updated: {item_details['last_updated']}")
         print("-" * 20)  # Separator for better readability
         

def update_stock(inventory, item_name, new_stock):
    """
    Updates the stock quantity for an existing item.
    """
    if item_name not in inventory:
        print(f"Error: Item '{item_name}' not found.")
        return
    # Update stock and timestamp
    inventory[item_name]['stock'] = new_stock
    inventory[item_name]['last_updated'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"Stock for '{item_name}' updated successfully.")

def search_by_category(inventory, category):
    """
    Returns a dictionary of items matching the given category.
    """
    matching_items = {}
    for item_name, item_data in inventory.items():
        if item_data['category'].lower() == category.lower():
            matching_items[item_name] = item_data
    return matching_items

def format_currency(amount):
    return "${:,.2f}".format(amount)

def low_stock_alert(inventory, low_threshold):
    """
    Finds all items with stock less than the threshold.
    """
    low_stock_items = {}
    for item_name, item_data in inventory.items():
        if item_data['stock'] < low_threshold:
            low_stock_items[item_name] = item_data
    return low_stock_items

def calculate_total_value(inventory):
    """
    Calculates total value by summing (price * stock) for all items.
    """
    total_value = 0
    for item_name, item_data in inventory.items():
        total_value += item_data['price'] * item_data['stock']
    return total_value

def display_inventory(inventory):
    """
    Prints the current inventory items in a formatted manner.
    """
    if not inventory:
        print("Inventory is empty.")
        return
    for item_name, item_data in inventory.items():
        print("--" * 10)
        print(f"Item: {item_name}")
        print(f"  Price: ${item_data['price']:.2f}")
        print(f"  Stock: {item_data['stock']}")
        print(f"  Category: {item_data['category']}")
        print(f"  Last Updated: {item_data['last_updated']}\n")
        # item_name += idx, item_name
        

# ============= TEST VALUES AND FUNCTION CALLS =============

# Adding sample items to the inventory
add_item(inventory, "Laptop", 1200.00, 5, "Electronics")
add_item(inventory, "Mouse", 25.00, 20, "Electronics")
add_item(inventory, "Keyboard", 75.00, 15, "Electronics")
add_item(inventory, "T-Shirt", 15.00, 50, "Clothing")
add_item(inventory, "Jeans", 40.00, 8, "Clothing")

list_inventory(inventory)

# Updating stock for an existing item
update_stock(inventory, "Laptop", 3)
list_inventory(inventory)

# Searching for items in a specific category
electronics = search_by_category(inventory, "Electronics")
print("\n:``== Electronics Category Items ==``:")
display_inventory(electronics)
print("--" * 10)

# Checking for low stock items (threshold: less than 5)
low_stock_items = low_stock_alert(inventory, 5)
print("\n:``== Low Stock Items (less than 5 units) ==``:")
display_inventory(low_stock_items)
print("--" * 10)

# Calculating total inventory value
total_value = calculate_total_value(inventory)
print(f"\nTotal Inventory Value: {format_currency(total_value)}\n")

# Display the full inventory
print(":``== Full Inventory ==``:")
display_inventory(inventory)


