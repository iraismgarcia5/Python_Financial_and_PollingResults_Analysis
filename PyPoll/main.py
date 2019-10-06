
import os
import csv

csvpath = os.path.join("C:\\Users\\irais\\OneDrive\\Desktop\\Resources\\election_data.csv")

total_votes = 0 
khan_total = 0
correy_total = 0
li_total = 0
otooley_total = 0


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    # print(csvreader)

    for row in csvreader:
        total_votes +=1

        if row[2] == "Khan":
            khan_total +=1
        elif row[2] == "Correy":
            correy_total +=1
        elif row[2] == "Li":
            li_total +=1
        elif row[2] == "O'Tooley":
            otooley_total +=1

candidate = ["Khan","Correy","Li","O'Tooley"]
vote_count = [khan_total,correy_total,li_total,otooley_total]

candidate_vote = dict(zip(candidate,vote_count))
winner = max(candidate_vote, key=candidate_vote.get)
# print(winner)

khan_percent = format(((khan_total/total_votes) * 100),'.3f')
correy_percent = format(((correy_total/total_votes) * 100),'.3f')
li_percent = format(((li_total/total_votes) * 100),'.3f')
otooley_percent = format(((otooley_total/total_votes) * 100),'.3f')

# print(otooley_percent)
# print(khan_percent)
# print(correy_percent)
# print(li_percent)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Khan: {khan_percent} ({khan_total})")
print(f"Correy: {correy_percent} ({correy_total})")
print(f"Li: {li_percent} ({li_total})")
print(f"O'Tooley: {otooley_percent} ({otooley_total})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


results = os.path.join("C:\\Users\\irais\\OneDrive\\Desktop\\python-challenge\\PyPoll\\results.txt")

with open(results,"w") as file:

    file.write("Election Results \n")
    file.write("----------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    file.write(f"Khan: {khan_percent} ({khan_total})\n")
    file.write(f"Correy: {correy_percent} ({correy_total})\n")
    file.write(f"Li: {li_percent} ({li_total})\n")
    file.write(f"O'Tooley: {otooley_percent} ({otooley_total})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")





