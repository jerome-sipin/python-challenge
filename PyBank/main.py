#Import modules
import os
import csv

#Create variables and initializes them 
totalMonths = 0
total = 0
avgChange = 0
greatestIncrease = 0
greatestIncreaseMonth = ""
greatestDecrease = 0
greatestDecreaseMonth = ""

#Locate budget file
budgetData = os.path.join('Resources', 'budget_data.csv')

#Reading budget file
with open(budgetData) as csvfile:
    
    budgetReader = csv.reader(csvfile, delimiter=",")

    next(budgetReader)

    for row in budgetReader:

        #Finds the amount of months in the budget data file
        totalMonths += 1

        #Calculates the total change in profit
        total = total + int(row[1])

        #Finds the greatest increase in profit
        if greatestIncrease < int(row[1]):

            greatestIncrease = int(row[1])
            greatestIncreaseMonth = row[0]

        #Finds the greatest decrease in profit
        if int(row[1]) < greatestDecrease and int(row[1]) <= 0:

            greatestDecrease = int(row[1])
            greatestDecreaseMonth = row[0]

#Calculates average change and rounds it to two decimals
avgChange = (total)/(totalMonths)
avgChange = round(avgChange, 2)

#Creates a new .txt file in the Analysis folder and writes in the console output into the file
f = open("Analysis/financial_analaysis.txt", "x")
f.write("Financial Analysis \n")
f.write("------------------------------------------ \n")
f.write(f'Total Months: {totalMonths} \n')
f.write(f'Total: ${total} \n')
f.write(f'Average Change: ${avgChange} \n')
f.write(f'Greatest Increase in profits: ${greatestIncrease}, on {greatestIncreaseMonth} \n')
f.write(f'Greatest Decrease in profits: ${greatestDecrease}, on {greatestDecreaseMonth} \n')
f.close

#Prints out variables to console
print(f'Financial Analysis')
print(f'------------------------------------------')
print(f'Total Months: {totalMonths}')
print(f'Total: ${total}')
print(f'Average Change: ${avgChange}')
print(f'Greatest Increase in profits: ${greatestIncrease}, on {greatestIncreaseMonth}')
print(f'Greatest Decrease in profits: ${greatestDecrease}, on {greatestDecreaseMonth}')
