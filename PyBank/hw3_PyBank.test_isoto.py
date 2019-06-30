#Download the data
import os
import csv

#set path
PyBank_csv = os.path.join("Resources", "budget_data.csv")

dates = []
prof_loss = []
changes = []


#PyBank: analyze records to calculate the following: 

# 1. Total # of months included in the Dataset

# 2. Net total amount of "Profit/Losses" over the entire period
   

# 3. Average of the changes in "Profit/Losses" over the entire period



# 4. The greatest increase in profits (date and amount) over the entire period



# 5. the greatest decrease in losses (date and amount) over the entire period



#print out the data!


with open(PyBank_csv, newline = '') as PyBank_csvfile:
    PyBank_csvreader = csv.reader(PyBank_csvfile, delimiter = ',') #specifies delimiter variable
    PyBank_csvheader = next(PyBank_csvreader) #want to see the headers!
    print(f"PyBank Header :{PyBank_csvheader}")

#PyBank: analyze records to calculate the following: 
# 
# # 1. Total # of months included in the Dataset

    for row in PyBank_csvreader:
        #month_year = str(row[0])
        dates.append(row[0]) 
        prof_loss.append(int(row[1]))
    
    previous = 0
    for num in prof_loss:
        #calculating the change variable
        change = num - previous
        changes.append(change)
        #previous = changes
        previous = num
        #print(change)
        #print(num)
        #print(previous)
changes.pop(0) 
average_change = sum(changes)/int(len(changes))
#print(changes.index(max(changes)))
#print(changes.index(min(changes)))

print("Financial Analysis") 
print("-----------------------------------------")
print(f"Total Months: {len(dates)}")
print(f"Total: ${str(sum(prof_loss))}") 
print(f"Average Change: ${str(average_change)}")
print(f"Greatest Increase in Profits: {dates[24]} (${str(max(changes))})")
print(f"Greatest Decrease in Profits: {dates[43]} (${str(min(changes))})")



       





# 2. Net total amount of "Profit/Losses" over the entire period



# 3. Average of the changes in "Profit/Losses" over the entire period



# 4. The greatest increase in profits (date and amount) over the entire period



# 5. the greatest decrease in losses (date and amount) over the entire period
