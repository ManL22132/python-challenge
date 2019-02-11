# First we'll import the os module
# This will allow us to create file paths across operating systems

import os
import csv

# file = '/Resources/election_data.csv'

poll_csv = os.path.join('..', 'C:\KU_Bootcamp\python-challenge\PyPoll\Resources', 'election_data.csv')
# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(poll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
    
    all_votes = 0
    temp_name = ""
    percent_vote = 0.00
    total_votes = 0

    for row in csvreader:
        all_votes += 1
        temp_name = (row[2])

        if ((row[2]) != temp_name):
            total_votes = 0
            percent_vote = (total_votes / all_votes) * 100
            temp_name = (row[2])
        else:
            total_votes = int(total_votes + 1)
            percent_vote = 0

    print(f"Election Results")
    print(f"-------------------------")
    print(f"Total votes: {all_votes}")
    print(f"-------------------------")
    print(f"{temp_name}: {percent_vote}% ({total_votes})")
    print(f"-------------------------")
    print(f"Winner: {temp_name}")

    f = open("C:\KU_Bootcamp\python-challenge\PyPoll\output2.txt", "a")
    f.write(f"Election Results")
    f.write(f"-------------------------")
    f.write(f"Total votes: {all_votes}")
    f.write(f"-------------------------")
    f.write(f"{temp_name}: {percent_vote}% ({total_votes})")
    f.write(f"-------------------------")
    f.write(f"Winner: {temp_name}")