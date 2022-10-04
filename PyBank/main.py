import os
from operator import index
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

print("Financial Analysis")

print('"-------------------------------"')

months = []
total_profits = []
changes_in_profits = 0
monthly_changes = []
previous_value = 0

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    csv_reader= next (csvreader)

    for row in csvreader:
        months.append(row[0])
        total_profits.append(row[1])
    print(len(months))

    total_profits = [int(x)for x in total_profits]
    total_profits_net = sum(total_profits)   

    print("Total: ", "$", total_profits_net)
for i in range(len(total_profits)-1):
    monthly_changes.append(total_profits[i+1]-total_profits[i])

average_changes = sum(monthly_changes)/len(monthly_changes)

num = average_changes
rounded = round(num, 2) 

print("Average Change:", "$", rounded)
greatest_increase = max(monthly_changes)
greatest_decrease = min(monthly_changes)
total_increase = monthly_changes.index(greatest_increase)
total_decrease = monthly_changes.index(greatest_decrease)
print("Greatest increase in profits over the entire period: ", 
months[total_increase + 1], "(","$",greatest_increase,")")

print("Greatest decrease in profits over the entire period: ", 
months[total_decrease + 1], "(","$",greatest_decrease,")")


output_file = os.path.join('Analysis', 'new.txt')

with open(output_file, "w") as f:


    f.write(f"Financial Analysis\n")
    f.write(f"-------------------------------\n")
    f.write(f"{len(months)}\n")
    f.write(f"Total:  ${total_profits_net}\n")
    f.write(f"Average Change: ${rounded}\n")
    f.write(f"Greatest increase in profits over the entire period:  {months[total_increase + 1]} (${greatest_increase})\n")
    f.write(f"Greatest increase in profits over the entire period:  {months[total_decrease + 1]} (${greatest_decrease})\n")
