# Import os and csv
import os
import csv
import statistics

# Make path to csv file for PyPoll
PyPollcsv = os.path.join("PyPoll", 'Resources', 'election_data.csv')

# Make path to output file
output_file = os.path.join("PyPoll", 'pollinganalysis.txt')

# read in the csvfile
with open(PyPollcsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Setting variables
    TotalVotes = 0
    Unique = []
    TotalCandidates = 0
    CandidateCount = []
    CandidateList = []
    CVotes = []
    VotePercent = []

    # Reading header row
    header = next(csvreader)

    # Read the first row
    firstrow = next(csvreader)
    TotalVotes = TotalVotes + 1
    

    #Iterate through the rows
    for row in csvreader:

        # count each additional row
        TotalVotes = TotalVotes + 1

        if row[2] not in Unique:
            Unique.append(row[2])

        CVotes.append(row[2])

    for candidate in Unique:
        CandidateCount.append(CVotes.count(candidate))
        VotePercent.append(round(CVotes.count(candidate)/TotalVotes*100,3))

    winner = Unique[CandidateCount.index(max(CandidateCount))]
    

output = (
    "Election Results\n"
    "--------------------------------\n"
    "Total Votes: " + str(TotalVotes) + "\n"
    "--------------------------------\n"
    for i in range(len(unique)):
        "f{unique[i]}: {percent[i]}% {CandidateCount[i]}\n"
    "---------------------------------\n"
    "Winner: Khan"
    "---------------------------------\n"
)

# export results to output file
with open(output_file, "w") as textfile: 
    textfile.write(output)