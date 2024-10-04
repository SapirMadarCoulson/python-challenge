# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""
# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("/Users/sapircoulson/python-challenge/PyBank/Resources/budget_data.csv")  # Input file path
file_to_output = os.path.join("/Users/sapircoulson/python-challenge/PyBank/analysis/budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
change = 0
avg_change = 0
increase = {"month": "", "amount": 0}
decrease = {"month": "", "amount": 0}
previous_net = None
net_change_list =[]
months =[]


# Open and read the csv
with open(file_to_load) as financial_data:
    csvreader = csv.reader(financial_data, delimiter=',')
    # Extract first row to avoid appending to net_change_list
    header = next(csvreader)
# Read each row of data after the header
    for row in csvreader:
        month = row[0]
# Track the total
        total_months += 1
        current_net = int(row[1])

        if previous_net is not None:
            net_change = current_net - previous_net
            net_change_list.append(net_change)
# Calculate the greatest increase in profits (month and amount)
            if net_change > increase["amount"]:
                increase["month"] = month
                increase["amount"] = net_change
        # Calculate the greatest decrease in losses (month and amount)
            if net_change < decrease["amount"]:
                decrease["month"] = month
                decrease["amount"] = net_change

        previous_net = current_net
        total_net += current_net


# Calculate the average net change across the months
if len(net_change_list) > 0:
    avg_change = sum(net_change_list) /len(net_change_list)
else:
    avg_change =0


# Generate the output summary
output = (
                  f" Financial Analysis\n"
                  f"------------------------------\n"
                  f"Total Mounths: {total_months}\n"
                  f"Total: ${total_net}\n"
                  f"Average Change: ${avg_change}\n"
                  f"Greatest Increase in Profits: {increase['month']} (${increase ['amount']})\n"
                  f"Greatest Decrease in Profits:  {decrease['month']} (${decrease ['amount']})\n"
                  )
# Print the output

print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
