# Personal Budget tracker

from datetime import datetime                # Import datetime module for date handling

# Global data structure to hold all budget data
# Structure:
# {
#   "YYYY-MM": {
#       "income": {category: amount, ...},
#       "expenses": {category: amount, ...},
#       "budgets": {category: limit, ...}
#   },
#   ...
# }
budget_data = {}

def load_from_txt():
    """
    Loads budget data from 'budget_data.txt'.
    Expects each line in the format:
    YYYY-MM-DD, category_type, category, amount   like  ; 2024-01-15, income, Salary, 3200
   
    """
    global budget_data  # Declare global scope to modify the outer variable
    try:
        # Open the file in read mode
        with open('budget_data.txt', 'r') as f:
            # Read each line in the file
            for line in f:
                line = line.strip()  # Remove space arount text 
                if not line:
                    continue  # Skip empty lines
                # Split line into four parts
                parts = line.split(', ')
                if len(parts) != 4:
                    continue  # Skip malformed lines
                # Unpack parts/attributes
                date_str, category_type, category, amount_str = parts
                # Convert date string to 'YYYY-MM' format for monthly grouping
                month = get_month_key(date_str)
                # Convert amount string to float
                amount = float(amount_str)
                # Initialize month if it does not exist
                if month not in budget_data:
                    budget_data[month] = {"income": {}, "expenses": {}, "budgets": {}}
                # Determine which sub-dictionary to store data in
                if category_type == 'income':
                    data_dict = budget_data[month]['income']
                elif category_type == 'expenses':
                    data_dict = budget_data[month]['expenses']
                elif category_type == 'budgets':
                    data_dict = budget_data[month]['budgets']
                else:
                    continue  # Skip unknown category types
                # Store the amount in the appropriate dictionary
                data_dict[category] = amount
    except FileNotFoundError:
        # If the file doesn't exist, initialize empty data
        # budget_data = {}
        print("File not found")

def save_to_txt():
    """
    Saves the current budget data to 'budget_data.txt' in the specified format.
    """
    with open('budget_data.txt', 'w') as f:
        # Loop through each month in the data
        for month, data in budget_data.items():
            # Convert 'YYYY-MM' back to 'YYYY-MM-DD' for record consistency
            date_str = datetime.strptime(month, '%Y-%m').strftime('%Y-%m-%d')
            # Loop through each category type
            for category_type in ['income', 'expenses', 'budgets']:
                # Loop through each category and amount
                for category, amount in data.get(category_type, {}).items():
                    # Format line for writing
                    line = f"{date_str}, {category_type}, {category}, {amount}\n"
                    f.write(line)  # Write line to file

def get_month_key(date_str):
    """
    Converts a date string 'YYYY-MM-DD' to 'YYYY-MM' for grouping.
    """
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')  # Parse date string
    return date_obj.strftime('%Y-%m')  # Return the 'YYYY-MM'

def add_income(date_str, category, amount):
    """
    Adds income for a specific date and category.
    """
    month = get_month_key(date_str)  # Get month key
    if month not in budget_data:
        # Initialize month if not present
        budget_data[month] = {"income": {}, "expenses": {}, "budgets": {}}
    # Access income dictionary for the month
    income = budget_data[month]["income"]
    # Add amount to existing or new entry
    income[category] = income.get(category, 0) + amount

def add_expense(date_str, category, amount):
    """
    Adds expense for a specific date and category.
    """
    month = get_month_key(date_str)
    if month not in budget_data:
        # Initializes the month if needed
        budget_data[month] = {"income": {}, "expenses": {}, "budgets": {}}
    # Access expenses dictionary
    expenses = budget_data[month]["expenses"]
    # Add amount to existing or new entry
    expenses[category] = expenses.get(category, 0) + amount

def set_budget_limit(date_str, category, limit):
    """
    Sets a budget limit for a category in a specific month.
    """
    month = get_month_key(date_str)
    if month not in budget_data:
        # Initialize month if missing
        budget_data[month] = {"income": {}, "expenses": {}, "budgets": {}}
    # Access budgets dictionary
    budgets = budget_data[month]["budgets"]
    # Set the limit for the category
    budgets[category] = limit

def analyze_month(month):
    """
    Analyzes data for a given month and returns summary info.
    """
    # Get data for the month, default to empty dicts if data isn't found
    data = budget_data.get(month, {})
    income = data.get("income", {})
    expenses = data.get("expenses", {})
    budgets = data.get("budgets", {})

    # Calculate total income and expenses
    total_income = sum(income.values())
    total_expenses = sum(expenses.values())
    # Calculate net savings
    net_savings = total_income - total_expenses
    # Calculate savings percentage
    savings_percent = (net_savings / total_income * 100) if total_income > 0 else 0     # calculates percentage of the total income by user saved in file
    # if no income was saved it shows 0%

    # Create a breakdown of expenses with percentages
    expense_breakdown = []
    for category, amount in expenses.items():
        percent = (amount / total_expenses * 100) if total_expenses > 0 else 0       # calcultes the percentage of the total expenses(gotten fron each expense)
        # if they are no expenses it shows 0%
        expense_breakdown.append((category, amount, percent)) # list of tuples with three elements
    # Return all computed data as a dictionary
    return {
        "total_income": total_income,
        "total_expenses": total_expenses,
        "net_savings": net_savings,
        "savings_percent": savings_percent,
        "expenses": expense_breakdown,
        "budgets": budgets
    }

def display_summary(month):
    """
    Prints a detailed summary report for a specific month.
    """
    analysis = analyze_month(month)  # Get analysis data
    # Print header
    print(f"=== PERSONAL BUDGET TRACKER ===")
    print(f"Month: {datetime.strptime(month, '%Y-%m').strftime('%B %Y')}\n")
    # Financial overview
    print("💰 FINANCIAL SUMMARY")
    print(f"Total Income: ${analysis['total_income']:.2f}")
    print(f"Total Expenses: ${analysis['total_expenses']:.2f}")
    print(f"Net Savings: ${analysis['net_savings']:.2f} ({analysis['savings_percent']:.1f}%)\n")
    # Expense breakdown with simple bar chart
    print("📊 EXPENSE BREAKDOWN")
    for category, amount, percent in analysis['expenses']:
        bar_length = int(percent // 2)  # Scale bar length
        bar = '█' * bar_length  # Create bar
        print(f"{category:12} {bar} {amount:.2f} ({percent:.1f}%)")
    # Budget alerts if expenses exceed set limits
    print("\n⚠️ BUDGET ALERTS:")
    for category, amount, percent in analysis['expenses']:
        limit = analysis['budgets'].get(category)
        if limit is not None:
            if amount > limit:
                over = amount - limit
                print(f"{category}: ${amount:.2f} over budget by ${over:.2f} ({(amount/limit)*100:.1f}%)")
            else:
                remaining = limit - amount
                print(f"{category}: ${amount:.2f} remaining of ${limit:.2f}")

# --- Example Usage ---

# Load existing data from the text file
load_from_txt()

# Add some sample data
add_income('2024-01-15', 'Salary', 3200)  # Add income
add_expense('2024-01-16', 'Food', 430)    # Add expense
add_expense('2024-01-16', 'Transport', 200)
set_budget_limit('2024-01-01', 'Food', 400)  # Set budget limits
set_budget_limit('2024-01-01', 'Transport', 150)

# Display the report for January 2024
display_summary('2024-01')

# Save all changes back to the text file
save_to_txt()
