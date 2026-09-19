# Main Interface

def maininterface():

    print("\n===== EXPENSE TRACKER =====")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")
    total = 0
    y = input("Choose your next action: ")

    if y == '1':
        return add_item()

    elif y == '2':
        print("YOUR EXPENSES ARE\n")
        for items in expenses:
            
            print(expenses[items],items)
        for i in expenses:
            total = total + expenses[i]
        print("TOTAL EXPENSE: ",total)
        return maininterface()

    elif y == '3':
        return

    else:
        print("Invalid choice. Please try again.")
        return maininterface()


# Store expenses in this dictionary

expenses = {}


# Get Integer Function

def get_int(prompt="Please enter an integer: "):

    while True:

        try:
            # Attempt to convert the input into an integer
            return int(input(prompt))

        except ValueError:
            # If a ValueError occurs, let the loop repeat
            print("Invalid input! That was not a whole number. Please try again.\n")


# Define ADD ITEM Function

def add_item():

    while True:

        item = input("ADD ITEM: ")

        expense = get_int("Amount Spent? ")

        expenses.update({item: expense})

        x = int(input(
            "Press 1 to add more, 2 for main menu, 3 to exit: "
        ))

        if x == 1:
            continue

        elif x == 3:
            break

        else:
            return maininterface()


# User Choice Function

def userinput():

    x = int(input(
        "Press 1 to add more, 2 for main menu, 3 to exit: "
    ))


# Start the program

maininterface()