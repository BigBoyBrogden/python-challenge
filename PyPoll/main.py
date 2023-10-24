import csv


total_votes = 0
candidate_votes = {}

file_path = 'Resources/election_data.csv'
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    csv_data = list(reader)
    csv_data = csv_data[1:]

    for row in csv_data:
        voter_id = row[0]
        county = row[1]
        candidate = row[2]

        total_votes = total_votes + 1

        if candidate in candidate_votes:
            candidate_votes[candidate] = candidate_votes[candidate] + 1
        else:
            candidate_votes[candidate] = 1

percentage_votes = {}
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    percentage_votes[candidate] = round(percentage, 3)

max_votes = 0
winner = ""
for candidate, votes in candidate_votes.items():
    if votes > max_votes:
        max_votes = votes
        winner = candidate

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {percentage_votes[candidate]}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

with open('analysis/election_results.txt', 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        output_file.write(f"{candidate}: {percentage_votes[candidate]}% ({votes})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")

print("Analysis saved to election_results.txt")
