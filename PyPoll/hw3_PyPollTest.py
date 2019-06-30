import os
import csv

PyPoll_csv = os.path.join("Resources", "election_data.csv")

#make empty dictionary


with open(PyPoll_csv, 'r') as csvfile:
    election_reader = csv.reader(csvfile, delimiter = ',')
    
    next(election_reader)

    for line in election_reader:
        print(line)

    

        #loop through the names of candidates and count the sum of people voting for them
        #make this into a forloop that goes through the data
        #for row in PyPoll_csvreader

   #     VoterID.append(row[0])
  #      County.append(row[1])
 #       Candidate.append(row[2])
#print(len(VoterID))



#You will be give a set of poll data called election_data.csv. 
# The dataset is composed of three columns: Voter ID, County, and Candidate. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:
    # The total number of votes cast: get the length of the voter ID

    # A complete list of candidates who received votes

    # The percentage of votes each candidate won

    # The total number of votes each candidate won

    # The winner of the election based on popular vote.


