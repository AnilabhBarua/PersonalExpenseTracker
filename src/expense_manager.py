expenses = []

def add_expense(amount, category, description):
    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }
    expenses.append(expense)
    return expenses
