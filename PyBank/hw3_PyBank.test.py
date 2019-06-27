#Download the data
#import os
#import csv
import pandas as pd

#set path

# find out what the encoding is so that you can see data with pandas
#PyBank_csv = os.path.join("Resources", "budget_data.csv")
#with open(PyBank_csv) as f:
    #print(f) #to find encoding, which is cp1252

#set path
PyBank_path = "Resources/budget_data.csv"
PyBank_df = pd.read_csv(PyBank_path, encoding="cp1252")

#look at the head of the data
PyBank_df.head()

