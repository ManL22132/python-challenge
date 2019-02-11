# First we'll import the os module
# This will allow us to create file paths across operating systems

import os
import csv

# file = '/Resources/budget_data.csv'

budget_csv = os.path.join('..', 'C:\KU_Bootcamp\python-challenge\PyBank\Resources', 'budget_data.csv')
# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    total_month = 0
    total_budget = 0.00
    t_average = 0.00
    t_pos = []
    g_increase = 0
    g_decrease = 0

    for row in csvreader:

        total_month += 1
        total_budget = total_budget + int(row[1])
        t_average = ((total_budget / total_month) / 12)

        t_pos.append(row[1])
    
g_increase = int(max(t_pos))
g_decrease = int(min(t_pos))

print(f"Financial Analysis")
print(f"===================================================")
print(f"Total month: {str(total_month)}")
print(f"Total budget: ${total_budget}")
print(f"Average change: ${t_average}")
print(f"Greatest increase in profit: {row[0]} ${g_increase}")
print(f"Greatest decrease in profit: {row[0]} ${g_decrease}")

f = open("C:\KU_Bootcamp\python-challenge\PyBank\output.txt", "a")
f.write(f"Financial Analysis")
f.write(f"===================================================")
f.write(f"Total month: {str(total_month)}")
f.write(f"Total budget: ${total_budget}")
f.write(f"Average change: ${t_average}")
f.write(f"Greatest increase in profit: {row[0]} ${g_increase}")
f.write(f"Greatest decrease in profit: {row[0]} ${g_decrease}")