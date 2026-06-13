import json

my_expenses = {}
#description = "key"
#amount = "value"

def read_file(): #reading the json file
    with open("expenses.json", "r") as file:
        global expenses
        expenses = json.load(file) #convert json to python dict
        return expenses

def write_file(): #writing/updating the file
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent = 4) #convert python to json

def delete_expense(): #delete an expense
    view_expenses()
    expense_to_delete = input("What expense you want to delete? ")
    if expense_to_delete in expenses:
        expenses.pop(expense_to_delete)
        print("Expense successfully deleted.")
    else:
        print("Expense not found.")
    write_file()


def add_expense(): #adding expense
    view_expenses()
    description = input("Enter description: ")
    amount = float(input("Enter the amount: "))
    expenses.update({f"{description}" : amount})
    print("Expense successfully added.")
    write_file()

def update_expense(): #update an expense
    view_expenses()
    expense_to_update = input("What expense you want to update? ")
    if expense_to_update in expenses:
        new_expense = input("What is the new amount? ")
        expenses[expense_to_update] = new_expense
        print("Expense successfully updated.")
    else:
        print("Expense not found.")
    write_file()
def view_expenses(): #view all expenses
    read_file()
    print("Expenses:")
    for key in expenses:
        print(f"{key}: {expenses[key]}")

running = True
while running:
    print("""
Welcome to expense tracker.
Choose what option you like:
1. View all expenses.
2. Add an expense.
3. Update an expense.
4. Delete an expense.
""")
    try:
        choice = int(input("Enter your choice (1, 2, 3, 4): "))
        if choice == 1:
            view_expenses()
        elif choice == 2:
            add_expense()
        elif choice == 3:
            update_expense()
        elif choice == 4:
            delete_expense()
        else:
            print("Invalid input.")
    except ValueError:
        print("Invalid input.")
    want_continue = input("Press any key to continue or 'N' to close the application.").upper
    if want_continue == "N":
        running = False
