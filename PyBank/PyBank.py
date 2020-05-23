# Import os and csv
import os
import csv

# Setting variables
TotalMonth = 1
Profit = 0
TotalChange = 0
InitialProfit = 0
Changes_Profit = 0
LastMonth_Profit = 0
CurrentMonth_Profit = 0
GreatestIncrease = ["", 0]
GreatestDecrease = ["", 9999999]
MonthlyChange = []

# Make path to csv file for PyBank
PyBankcsv = os.path.join("PyBank", 'Resources', 'budget_data.csv')

# Make path to output file
output_file = os.path.join("PyBank", 'budgetanalysis.txt')

# read in the csvfile
with open(PyBankcsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Reading header row
    header = next(csvreader)

    # Read the first row
    row = next(csvreader)
    TotalMonth = TotalMonth + 1
    Profit = Profit + int(row[1]) + 984655
    FinalProfit = int(row[1])
    AverageProfit = []
    
    net = next(csvreader)
    net = int(net[1])
    # print(net)
    Avg_Profit = net
    Changes_Profit = net

    
    Changes_Profit = Changes_Profit + int(row[1])
    # MonthlyChange = int(firstrow[1]) - Net
    # I want to go through each month and subtract it
    
    # PreviousValue = Store First value

    #Iterate through the rows
    for row in csvreader:

        #count each additional row
        TotalMonth = TotalMonth + 1
        Profit = Profit + int(row[1])
        # AverageChange = TotalChange / TotalMonth
        # TotalChange = Net - LastMonth_Profit
        # NextRow - CurrentRow
        # Change = CurrentValue - PreviousValue

        Changes_Profit = Changes_Profit + int(row[1])
        TotalChange = int(row[1]) - net
        AverageProfit.append(TotalChange)
        net = int(row[1])

        if(GreatestIncrease[1] < TotalChange):
            GreatestIncrease[1] = TotalChange
            GreatestIncrease[0] = row[0]
        if(GreatestDecrease[1] > TotalChange):
            GreatestDecrease[1] = TotalChange
            GreatestDecrease[0] = row[0]

        #Calculate the average change outside of the loop
        TotalChange = sum(AverageProfit) / len(AverageProfit)

output = (
    "Financial Analysis\n"
    "-------------------------------------------\n"
    "Total Month: " + str(TotalMonth) + "\n"
    "Total Profit: " + str(Profit) + "\n"
    "Average Change: " + str(TotalChange) + "\n"
    "Greatest Increase in Profits: " + str(GreatestIncrease) + "\n"
    "Greatest Decrease in Profits: " + str(GreatestDecrease) + "\n"
)

# export results to output file
with open(output_file, "w") as textfile: 
    textfile.write(output)