import os
import csv

# Establish path to data
csvpath = os.path.join("raw_data", "election_data.csv")

# Create a variable for the total number of votes
total_votes = 0
candidate_winner = 0

# Create a list for candidate names
candidate_list = []
candidate_name = []

# Create a list for counts of and percent of votes per candidate
candidate_vote = [0, 0, 0, 0]
candidate_vote_percent = [0, 0, 0, 0]

# Read csv file and designate a header row
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    for row in csvreader:
        # Calculate total votes 
        total_votes += 1
        candidate_list.append(str(row[2]))

    for row[2] in candidate_list:
        if row[2] not in candidate_name:
            candidate_name.append(row[2])
        if row[2] == candidate_name[0]:
            candidate_vote[0] += 1
        elif row[2] == candidate_name[1]:
            candidate_vote[1] += 1
        elif row[2] == candidate_name[2]:
            candidate_vote[2] += 1
        elif row[2] == candidate_name[3]:
            candidate_vote[3] += 1

candidate_results = dict(zip(candidate_name, candidate_vote))

winner = max(candidate_results, key=lambda k: candidate_results[k])

candidate_vote_percent[0] = round(100 * (candidate_vote[0] / total_votes), 2)
candidate_vote_percent[1] = round(100 * (candidate_vote[1] / total_votes), 2)
candidate_vote_percent[2] = round(100 * (candidate_vote[2] / total_votes), 2)
candidate_vote_percent[3] = round(100 * (candidate_vote[3] / total_votes), 2)

print("Election Results")
print("---------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------")
print(f"{candidate_name[0]}: {candidate_vote[0]} ({candidate_vote_percent[0]}%)")
print(f"{candidate_name[1]}: {candidate_vote[1]} ({candidate_vote_percent[1]}%)")
print(f"{candidate_name[2]}: {candidate_vote[2]} ({candidate_vote_percent[2]}%)")
print(f"{candidate_name[3]}: {candidate_vote[3]} ({candidate_vote_percent[3]}%)")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

print(f"Election Results", file=open("results/pypoll_nopandas_MOSHER_2019.txt", "w"))
print(f"--------------------------", file=open("results/pypoll_nopandas_MOSHER_2019.txt", "a"))
print(f"Total Votes: {total_votes}", file=open("results/pypoll_nopandas_MOSHER_2019.txt", "a"))
print("---------------------------", file=open("results/pypoll_nopandas_MOSHER_2019.txt", "a"))
print(f"{candidate_name[0]}: {candidate_vote[0]} ({candidate_vote_percent[0]}%)", file=open("results/pypoll_nopandas_MOSHER_2019.txt", "a"))
print(f"{candidate_name[1]}: {candidate_vote[1]} ({candidate_vote_percent[1]}%)", file=open("results/pypoll_nopandas_MOSHER_2019.txt", "a"))
print(f"{candidate_name[2]}: {candidate_vote[2]} ({candidate_vote_percent[2]}%)", file=open("results/pypoll_nopandas_MOSHER_2019.txt", "a"))
print(f"{candidate_name[3]}: {candidate_vote[3]} ({candidate_vote_percent[3]}%)", file=open("results/pypoll_nopandas_MOSHER_2019.txt", "a"))
print("---------------------------", file=open("results/pypoll_nopandas_MOSHER_2019.txt", "a"))
print(f"Winner: {winner}", file=open("results/pypoll_nopandas_MOSHER_2019.txt", "a"))
print("---------------------------", file=open("results/pypoll_nopandas_MOSHER_2019.txt", "a"))