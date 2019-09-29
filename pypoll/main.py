import os
import pandas as pd

# Establish path to data
election_data_path = os.path.join('raw_data', 'election_data.csv')

# Read the csv file
election_data = pd.read_csv(election_data_path)

# Remove ID number (sensitive info and is not needed for the calculations)
without_ID = election_data[["County", "Candidate"]]

# Calculate the total amount of votes
total_votes = without_ID["Candidate"].count()

# Group by candidate and calculate total number of votes per candidate
candidates = (without_ID.groupby(["Candidate"]).count()).reset_index()

# Reorder, candidate with the highest is at the top
reorder_candidate = candidates.sort_values(["County"], ascending=False)

# Save the name of the winner for later
winner = reorder_candidate.iloc[0,0]

# Calculate the percent of the total vote for each candidate
reorder_candidate["%"] = (reorder_candidate["County"]/total_votes)*100

# Rename to 'County' to 'Number of the Votes' (as they were counted in groupby)
reorder_candidate.rename(columns={"County" : "# of Votes"}, inplace=True)

# Make the 'Candidate' column the index
final_results = reorder_candidate.set_index("Candidate")
# Format percent column so it looks nicer
final_results["%"] = final_results["%"].map("{:.0f}%".format)

print("------------------------------------")
print("Election Results")
print("------------------------------------")
print(f"Votes: {str(total_votes)}")
print("------------------------------------")
print(final_results)
print("------------------------------------")
print(f"Winner: {str(winner)}")
print("------------------------------------")

final_results.to_csv("results/pypoll_final_results_MOSHER.csv", index=True, header=True)