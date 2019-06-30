import os
import csv

#set path
PyBank_csv = os.path.join("Resources", "budget_data.csv")

#make empty lists
dates = []
prof_loss = []
changes = []

with open(PyBank_csv, newline = '') as PyBank_csvfile:
    PyBank_csvreader = csv.reader(PyBank_csvfile, delimiter = ',') #specifies delimiter variable
    PyBank_csvheader = next(PyBank_csvreader) #want to see the headers!
    print(f"PyBank Header :{PyBank_csvheader}")

#PyBank: analyze records to calculate the following: 

    for row in PyBank_csvreader:
        dates.append(row[0])  #append to empty lists
        prof_loss.append(int(row[1]))
    
    #start your count
    previous = 0
    for num in prof_loss:
        #calculating the change variable
        change = num - previous
        changes.append(change)
        previous = num
changes.pop(0) 
#get the average 
average_change = sum(changes)/int(len(changes))

#print out the data!
print("Financial Analysis") 
print("-----------------------------------------")
# 1. Total # of months included in the Dataset
print(f"Total Months: {len(dates)}")
# 2. Net total amount of "Profit/Losses" over the entire period
print(f"Total: ${str(sum(prof_loss))}") 
# 3. Average of the changes in "Profit/Losses" over the entire period
print(f"Average Change: ${str(average_change)}")
# 4. The greatest increase in profits (date and amount) over the entire period
print(f"Greatest Increase in Profits: {dates[24]} (${str(max(changes))})")
# 5. the greatest decrease in losses (date and amount) over the entire period
print(f"Greatest Decrease in Profits: {dates[43]} (${str(min(changes))})")

