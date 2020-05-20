# Import os and csv
import os
import csv

# Make path to csv file for PyBank
PyBankcsv = os.path.join('Resources', 'budget_data.csv')

# read in the csvfile
with open(PyBankcsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Setting variables
TotalMonth = 0
Profit = 0
RevenueChange = 0