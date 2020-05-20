# Import os and csv
import os
import csv

# Setting variables
TotalMonth = 0
Profit = 0
RevenueChange = 0

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
    firstrow = next(csvreader)
    TotalMonth = TotalMonth + 1
    Profit = Profit + int(firstrow[1])

    #Iterate through the rows
    for row in csvreader:

        #count each additional row
        TotalMonth = TotalMonth + 1
        Profit = Profit + int(row[1])
        

output = (
    "financial analysis\n"
    "-------------------------------\n"
    "Total Month: " + str(TotalMonth) + "\n"
    "Total Profit: " + str(Profit) + "\n"
    "Average Change" + str("Add Variable") + "\n"
    "Greatest Increase in Profits" + str("Add Variable") + "\n"
    "Greatest Decrease in Profits" + str("Add Variable") + "\n"
)

# export results to output file
with open(output_file, "w") as textfile: 
    textfile.write(output)