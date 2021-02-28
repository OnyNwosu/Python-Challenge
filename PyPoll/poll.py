import os
import csv

Election_Data = os.path.join('..', 'Resources', 'election_data.csv')
Candidates = []
Number_Votes = []
Percent_Votes = []
Total_Votes = 0

with open(election_data) as csvfile
    csvreader = csv.reader(csvfile, delimiter = ",")
    cvsheader = next(csvreader)
    for row in csvreader
    Total_Votes +=1

    if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
    else:
        index = candidates.index(row[2])
        num_votes[index] += 1

    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)

winner = max(num_votes)
index = num_votes.index(winner)
winning_candidate = candidates[index]

print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

output = output.txt
with open(output, "w") as new: