#Download the data
import os
import csv

#set path
PyBank_csv = os.path.join("Resources", "budget_data.csv")

dates = []
prof_loss = []


#PyBank: analyze records to calculate the following: 

# 1. Total # of months included in the Dataset
#def PyBank_funct(PyBank_data): 

         #doing it for one and not all of them - str(PyBank_data[0]) 

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
        
        length = len(prof_loss)
        total = sum(prof_loss)
        average_change = total/length 


        
print(prof_loss)
print("Financial Analysis") 
print("-----------------------------------------")
print(f"Total Months: {len(dates)}")
print(f"Total: ${str(sum(prof_loss))}") 
print(f"Average Change: ${str(average_change)}")


       





# 2. Net total amount of "Profit/Losses" over the entire period



# 3. Average of the changes in "Profit/Losses" over the entire period



# 4. The greatest increase in profits (date and amount) over the entire period



# 5. the greatest decrease in losses (date and amount) over the entire period
