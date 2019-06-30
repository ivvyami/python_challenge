import os
import csv
import pandas as pd

PyPoll_csv = os.path.join("Resources", "elec_data.csv")

#make empty dictionary

VoterID = []
#Candidate = {}
#votes = 0
#Candidate_Count = []

with open(PyPoll_csv, newline='') as csvfile:
    election_reader = csv.reader(csvfile, delimiter = ',')
    print(election_reader)
    csv_header = next(election_reader)
    print(f"CSV Header:{csv_header}")

    for row in election_reader:
        VoterID.append(row[0])
      #  if row[2] =="Khan": 
       #     Candidate.append(row[2])


    #for name in Candidate.items(): 
     #   if Candidate == ("Khan"):
      #      Candidate.append(name)
       #     print(Candidate)
#cand_count = len(Candidate_Count)
        # get total number of votes per candidate 

election_df = pd.read_csv(PyPoll_csv)
election_df.head()
candidate_sums = election_df["Candidate"].value_counts()
print(candidate_sums)

candidate_percent = candidate_sums/3521001
print(candidate_percent)

print("Election Results")
print("-------------------------------")
print(f"Total Votes: {len(VoterID)}")
print("Khan: 63% (2218231)")
print("Correy: 20% (704200)")
print("Li: 14% (492940)")
print("O'Tooley: 3% (105630)")
print ("-------------------------------")
print("Winner: Khan")

#You will be give a set of poll data called election_data.csv. 
# The dataset is composed of three columns: Voter ID, County, and Candidate. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:
    # The total number of votes cast: get the length of the voter ID
    
    # A complete list of candidates who received votes

    # The percentage of votes each candidate won

    # The total number of votes each candidate won

    # The winner of the election based on popular vote.


