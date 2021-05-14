# Import dependencies fooff
import csv
import os

# Assign variables to file open and save paths
file_open_path = 'Resources/election_results.csv'
file_save_path = os.path.join("Analysis", "election_analysis.txt")

# Initialize variables
total_votes = 0
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# open election_results.csv
with open(file_open_path) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read & print header row
    headers = next(file_reader)
    #print(headers)

    # Get total number of votes (total_votes)
    for row in file_reader:
        total_votes += 1

        # Get list candidates who got votes 
        candidate_name = row[2]
        if candidate_name not in candidate_options:

            # Add candidate name to list of candidates
            candidate_options.append(candidate_name)

            # Begin tracking candidate vote count
            candidate_votes[candidate_name] = 0

        # Tally candidate votes
        candidate_votes[candidate_name] +=1

# Save output to election_analysis.txt
with open(file_save_path, "w") as txt_file:

    # Get total votes
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    )

    # Print total votes to terminal & .txt file
    print(election_results, end="")
    txt_file.write(election_results)

    # Determine vote totals & percentage of candidates
    for candidate_name in candidate_options:
        votes = candidate_votes[candidate_name]
        vote_percentage = (float(votes)/float(total_votes))*100

        # Get results for each candidate & print
        candidate_results = f"{candidate_name}: {vote_percentage}%, {votes}\n"
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine highest vote & winner
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    # Summarize the winner & print to terminal & .txt file
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)



