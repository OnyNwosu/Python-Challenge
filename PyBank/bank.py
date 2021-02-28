import os
import csv

file = os.path.join("..", "Bank CSV File", "budget_data.csv")
with open("budget_data.csv", "b") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",") 
    header = next(csvreader)
    Month_Count = []
    Profit = []
    Change_In_Profit = []

    for row in csvreader
        Month_Count.append(row[0])
        Profit.append(row[1])
    for i in range(len(Profit)-1):
        Change_In_Profit.append(Profit[i+1]-Profit[i])
        