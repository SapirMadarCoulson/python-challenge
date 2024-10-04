# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("/Users/sapircoulson/python-challenge/PyPoll/Resources/election_data.csv")  # Input file path
file_to_output = os.path.join("/Users/sapircoulson/python-challenge/PyPoll/analysis/results.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates_list = {}
# Winning Candidate and Winning Count Tracker
winner = {"name": "", "votes": 0}

# Open the CSV file and process it
with open(file_to_load, 'r') as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        # Increment the total vote count
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates_list:
            candidates_list[candidate_name] = 0

        # Add a vote to the candidate's count
        candidates_list[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    # Print the total vote count (to terminal)
    output_total_votes = f"Total Votes: {total_votes}\n"

    # Write the total vote count to the text file
    txt_file.write(f"Election Results\n")
    txt_file.write(f"------------------------------\n")
    txt_file.write(output_total_votes)
    txt_file.write(f"------------------------------\n")

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate, votes in candidates_list.items():
        # Get the vote count and calculate the percentage
        vote_percentage = (votes / total_votes) * 100
         # Print and save each candidate's vote count and percentage
        output_candidate = f"{candidate}: {vote_percentage:.3f}% ({votes} votes)\n"

        # Save the winning candidate summary to the text file
        txt_file.write(output_candidate)

        if votes > winner["votes"]:
            winner["name"] = candidate
            winner["votes"] = votes


        # Generate and print the winning candidate summary
    output_winner = f"Winner: {winner['name']}\n"

    txt_file.write(f"------------------------------\n")
    txt_file.write(output_winner)
    txt_file.write(f"------------------------------\n")

# Generate and print the winning candidate summary
print(f"Election Results\n")
print(f"------------------------------\n")
print(output_total_votes)
print(f"------------------------------\n")
for candidate, votes in candidates_list.items():
    vote_percentage = (votes / total_votes) * 100
    print(f"{candidate}: {vote_percentage:.3f}% ({votes} votes)")
print(f"------------------------------\n")
print(output_winner)
print(f"------------------------------\n")
