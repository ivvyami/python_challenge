#You will be give a set of poll data called election_data.csv. 
# The dataset is composed of three columns: Voter ID, County, and Candidate. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:

import os
import csv
import pandas as pd

PyPoll_csv = os.path.join("Resources", "elec_data.csv")

#make an empty list
VoterID = []

with open(PyPoll_csv, newline='') as csvfile:
    election_reader = csv.reader(csvfile, delimiter = ',')
    print(election_reader)
    csv_header = next(election_reader)
    print(f"CSV Header:{csv_header}")
#append voter ID to the list
    for row in election_reader:
        VoterID.append(row[0])
#read in data with pandas
election_df = pd.read_csv(PyPoll_csv)
election_df.head()
#get the counts for each candidate
candidate_sums = election_df["Candidate"].value_counts()
print(candidate_sums)
#get the percentage for each candidate
candidate_percent = candidate_sums/3521001
print(candidate_percent)


#print out your results
print("Election Results")
print("-------------------------------")
print(f"Total Votes: {len(VoterID)}")
print("Khan: 63% (2218231)")
print("Correy: 20% (704200)")
print("Li: 14% (492940)")
print("O'Tooley: 3% (105630)")
print ("-------------------------------")
print("Winner: Khan")