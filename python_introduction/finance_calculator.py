income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your monthly expenses: "))
savings = income - expenses
projected_Savings = (savings * 12 + (savings * 12 * 0.05))
print(f"Your projected savings for the year is: {projected_Savings}")