import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    Month_Count = []
    Profit = []
    Change_In_Profit = []

    for row in csvreader:
        Month_Count.append(row[0])
        Profit.append(row[1])
    for i in range(len(Profit)-1):
        Change_In_Profit.append(Profit[i+1]-Profit[i])

increase = max(Change_In_Profit)
decrease = min(Change_In_Profit)

Month_Increase = Change_In_Profit.index(max(Change_In_Profit))+1
Month_Decrease = Change_In_Profit.index(min(Change_In_Profit))+1

print("Financial Analysis")
print("__________________________")
print(f"Total Months:{len(Month_Count)}")
print(f"Total: ${sum(Profit)}")
print(f"Average Change: {round(sum(Change_In_Profit)/len(Change_In_Profit),2)}")
print(f"Greatest Increase in Profits: {Month_Count[Month_Increase]}(${(str(increase))})")
print(f"Greatest Decrease in Profits: {Month_Count[Month_Decrease]}(${(str(decrease))})")

output = output.txt
with open(output, "w") as new:
    new.write("Financial Analysis")
    new.write("____________________")
    new.write(f"Total Months:{len(Month_Count)}")
    new.write(f"Total: ${sum(Profit)}")
    new.write(f"Average Change: {round(sum(Change_In_Profit)/len(Change_In_Profit),2)}")
    new.write(f"Greatest Increase in Profits: {Month_Count[Month_Increase]}(${(str(increase))})")
    new.write(f"Greatest Decrease in Profits: {Month_Count[Month_Decrease]}(${(str(decrease))})")