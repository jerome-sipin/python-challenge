#Import modules
import os
import csv

totalMonths = 0
total = 0
avgChange = 0
greatestIncrease = 0
greatestIncreaseMonth = ""
greatestDecrease = 0
greatestDecreaseMonth = ""

budgetData = os.path.join('Resources', 'budget_data.csv')

with open(budgetData) as csvfile:
    
    budgetReader = csv.reader(csvfile, delimiter=",")

    for row in budgetReader:

        totalMonths += 1
        total = total + int(row[1])

        if greatestIncrease < row[1]:

            greatestIncrease = row[1]
            greatestIncreaseMonth = row[0]

        if row[1] < greatestDecrease & row[1] <= 0:

            greatestDecrease = row[1]
            greatestDecreaseMonth = row[0]

avgChange = total/totalMonths

print(f'{totalMonths}')
print(f'{total}')
print(f'{avgChange}')
print(f'{greatestIncrease} {greatestIncreaseMonth}')
print(f'{greatestDecrease} {greatestDecreaseMonth}')
