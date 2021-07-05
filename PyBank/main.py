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

    next(budgetReader)

    for row in budgetReader:

        totalMonths += 1
        total = total + int(row[1])

        if greatestIncrease < int(row[1]):

            greatestIncrease = int(row[1])
            greatestIncreaseMonth = row[0]

        if int(row[1]) < greatestDecrease and int(row[1]) <= 0:

            greatestDecrease = int(row[1])
            greatestDecreaseMonth = row[0]

avgChange = (total)/(totalMonths)

print(f'Financial Analysis')
print(f'------------------------------------------')
print(f'Total Months: {totalMonths}')
print(f'Total: ${total}')
print(f'Average Change: ${avgChange}')
print(f'Greatest Increase in profits: ${greatestIncrease}, on {greatestIncreaseMonth}')
print(f'Greatest Decrease in profits: ${greatestDecrease}, on {greatestDecreaseMonth}')
