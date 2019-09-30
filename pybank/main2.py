import os
import csv

# Establish path to data
csvpath = os.path.join("raw_data", "budget_data.csv")

# Create a variable for the total months in the dataset
total_months = 0
# Create a variable to add to the beginning of the change in profits list
variable_for_start_of_change = 0

# Create lists for profits/losses, date, and for the change in profits per month
profits_list = []
date_list = []
change_in_profit_list = []

# Read csv file and designate a header row
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    for value in csvreader:
        # Calculate total months
        total_months += 1
        # Add profits/losses values to a list, and add dates to another list
        profits_list.append(int(value[1]))
        date_list.append(str(value[0]))

# Calculate total profits/losses
total_profits = round(sum(profits_list), 2)

# Calculate change in profits/losses and add to a list  
for i in range(1,len(profits_list)):
    change_in_profit = profits_list[i] - profits_list[i-1]
    change_in_profit_list.append(change_in_profit)

# Calculate the average in the changes of profits and losses
average_change = round(sum(change_in_profit_list) / len(change_in_profit_list), 2)

# Add a variable to the beginning of the list of profit changes
change_in_profit_list.insert(0,variable_for_start_of_change)

# Calculate the greatest increase and greatest decrease in profits
greatest_increase = max(change_in_profit_list)
greatest_decrease = min(change_in_profit_list)

# Create a dictionary from the list of dates (the key) and the changes in profit (the value)
profit_change_results = dict(zip(date_list, change_in_profit_list))

# Determine the months of the greatest profits and greatest losses
greatest_increase_date = max(profit_change_results, key=lambda k: profit_change_results[k])
greatest_decrease_date = min(profit_change_results, key=lambda k: profit_change_results[k])

# Print results
print("Financial Analysis")
print("-----------------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profits}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: ${greatest_increase} ({greatest_increase_date})")
print(f"Greatest Decrease in Profits: ${greatest_decrease} ({greatest_decrease_date})")
print("-----------------------------------------------------")

# Save results to a text file
print("Financial Analysis", file=open("results/pybank_nopandas_MOSHER_2019.txt", "w"))
print("-----------------------------------------------------", file=open("results/pybank_nopandas_MOSHER_2019.txt", "a"))
print(f"Total Months: {total_months}", file=open("results/pybank_nopandas_MOSHER_2019.txt", "a"))
print(f"Total: ${total_profits}", file=open("results/pybank_nopandas_MOSHER_2019.txt", "a"))
print(f"Average Change: ${average_change}", file=open("results/pybank_nopandas_MOSHER_2019.txt", "a"))
print(f"Greatest Increase in Profits: ${greatest_increase} ({greatest_increase_date})", file=open("results/pybank_nopandas_MOSHER_2019.txt", "a"))
print(f"Greatest Decrease in Profits: ${greatest_decrease} ({greatest_decrease_date})", file=open("results/pybank_nopandas_MOSHER_2019.txt", "a"))
print("-----------------------------------------------------", file=open("results/pybank_nopandas_MOSHER_2019.txt", "a"))