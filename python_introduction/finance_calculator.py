monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
projected_savings = (monthly_savings * 12 + (monthly_savings * 12 * 0.05))
print(f"Your projected savings for the year is: {projected_savings}")