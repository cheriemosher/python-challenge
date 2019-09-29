import os
import pandas as pd

# Establish path to data
budget_data_path = os.path.join('raw_data', 'budget_data.csv')

# Read the csv file
budget_data = pd.read_csv(budget_data_path)

#create list, for row in _____, change is equal to i and i - 1
#append change to the list

# Calculate the total number of months
total_months = budget_data["Date"].count()

# Calculate the total in the budget
total_budget = budget_data["Profit/Losses"].sum()

# Calculate the average in profits/losses
# NOT THE SAME AS THE EXAMPLE
average_change = round(budget_data["Profit/Losses"].mean(), 2)

greatest_increase = budget_data.loc[budget_data["Profit/Losses"].idxmax()]
increase_date_result = greatest_increase.get(key = "Date")
increase_result = greatest_increase.get(key = "Profit/Losses")


greatest_decrease = budget_data.loc[budget_data["Profit/Losses"].idxmin()]
print(greatest_decrease)
decrease_date_result = greatest_decrease.get(key = "Date")
decrease_result = greatest_decrease.get(key = "Profit/Losses")

print("-----------------------------------------------------")
print("Financial Analysis")
print("-----------------------------------------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_budget)}")
print(f"Average Change: ${str(average_change)}")
print(f"Greatest Increase in Profits: {str(increase_date_result)} (${str(increase_result)})")
print(f"Greatest Decrease in Profits: {str(decrease_date_result)} (${str(decrease_result)})")
print("-----------------------------------------------------")

