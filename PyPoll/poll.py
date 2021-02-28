import os
import csv

Election_Data = os.path.join('..', 'Resources', 'election_data.csv')
Candidates = []
Candidate_List = []
Number_Votes = []
Percent_Votes = []
Total_Votes = 0

csvpath = os.path.join('Resources', 'election_data')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    cvsheader = next(csvreader)
    for row in csvreader
    Total_Votes +=1

    if row[2] not in candidates:
            Candidate_List.append(row[2])
            index = Candidates.index(row[2])
            Number_Votes.append(1)
    else:
        index = candidates.index(row[2])
        Number_Votes[index] += 1

    for Total_Votes in Number_Votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)

Winner = max(Number_Votes)
index = Number_Votes.index(winner)
Winning_Candidate = Candidates[index]

print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(Candidates)):
    print(f"{Candidates[i]}: {str(Percent_Votes[i])} ({str(Number_Votes[i])})")
print("--------------------------")
print(f"Winner: {Winning_Candidate}")
print("--------------------------")

output = output.txt
with open(output, "w") as txt_file:
    txt_file.write("Election Results")
    txt_file.write("--------------------------")
    txt_file.write(f"Total Votes: {str(total_votes)}")
    txt_file.write("--------------------------")
    txt_file.write(f"{Candidates[i]}: {str(Percent_Votes[i])} ({str(Number_Votes[i])})")
    txt_file.write("--------------------------")
    txt_file.write("--------------------------")
    txt_file.write(f"Winner: {Winning_Candidate}")
    txt_file.write("--------------------------")