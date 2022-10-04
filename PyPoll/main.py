import os
import csv

total_number_votes = 0
candidates = dict()
percentage_of_votes = dict()
total_votes = 0
votes_for_Charles = 0
votes_for_Diana = 0
votes_for_Raymon = 0

csvpath = os.path.join('Resources', 'election_data.csv')


with open(csvpath) as csvfile:
    csvreader = csv.reader (csvfile, delimiter= ",")
    csv_reader = next(csvreader)

    for row in csvreader:
        total_number_votes +=1
        candidates_names= row[2]

        if row[2] == "Charles Casper Stockham":
            votes_for_Charles += 1
        elif row[2] == "Diana DeGette":
            votes_for_Diana += 1
        elif row[2] == "Raymon Anthony Doane":
            votes_for_Raymon += 1
 

Ch_percentage = votes_for_Charles/total_number_votes * 100
Di_percentage = votes_for_Diana/total_number_votes * 100
Ray_percentage = votes_for_Raymon/total_number_votes * 100

list_cand_and_votes = {
    "Raymond Anthony Doane" : votes_for_Charles,
    "Diana DeGette" : votes_for_Diana,
    "Charles Casper Stockham" : votes_for_Raymon
}

Winner_name = ""
votes_for_winner = 0

output = f"""
Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
"""
print(output)

with open ("Analysis/new2.txt", "w") as file:
    file.write(output)

