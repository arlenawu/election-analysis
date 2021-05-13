# Import datetime
import datetime as dt
#now = dt.datetime.now()
#print("The time is ", now)
import csv
import os

# Assign variables to file open and save paths
file_open_path = 'Resources/election_results.csv'
file_save_path = os.path.join("Analysis", "election_analysis.txt")

# open election_results.csv
with open(file_open_path) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read & print header row
    headers = next(file_reader)
    print(headers)
    #for row in file_reader:
    #    print(row)


# save output to election_analysis.txt
with open(file_save_path, "w") as txt_file:

    txt_file.write("Arapahoe\nDenver\nJefferson")

#Data to retrieve
# 1. total # votes cast
# 2. complete list of candidates
# 3. % of votes for each candidate
# 4. total # votes for each candidate
# 5. winner of election

