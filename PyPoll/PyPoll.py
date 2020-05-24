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
    Khan = []
    Correy = []
    Li = []
    OTooley = []
    Candidates = []


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

print("Election Results")
print("--------------------------")
print(f"Total Results: {TotalVotes}")
for i in range(len(Unique)):
    print(f"{Unique[i]}: {VotePercent[i]}% ({CandidateCount[i]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")


poll_output_file = os.path.join("pollinganalysis.txt")
with open (poll_output_file, 'w') as txtfile:

    txtfile.write("Election Results\n")
    txtfile.write("--------------------------\n")
    txtfile.write(f"Total Results: {TotalVotes}\n")
    for i in range(len(Unique)):
        txtfile.write(f"{Unique[i]}: {VotePercent[i]}% ({CVotes[i]})\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("---------------------------\n")
