import os
import csv

total_votes = 0
candidate = []
candidate_list = []
candidate_votes = {}
winner = ""
winning_count = 0



with open('election_data.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',')

    header = next(reader)
#The total number of votes cast
    for row in reader:
        total_votes = total_votes+1
        #A complete list of candidates who received votes
        candidate = row[2]
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidate_votes[candidate] = 0

        candidate_votes[candidate] = candidate_votes[candidate]+1

with open('PyPoll.txt', "w") as text_file:
#The total number of votes each candidate won
    election_result = (
        f"\nElection Results"f"\n------------------------"f"\nTotal Votes: {total_votes}"f"\n---------------------")
    print(election_result)
    text_file.write(election_result)

    for candidate in candidate_votes:
        #The percentage of votes each candidate won
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes)/float(total_votes)*100

        if (votes > winning_count):
            winning_count = votes
            winner = candidate

        output = (f"\n{candidate}: {vote_percentage:.3f}% ({votes})")
        print(output, end="")
        text_file.write(output)
        #The winner of the election based on popular vote.
    winner = (
        f"\n-----------------------"f"\nWinner: {winner}"f"\n-----------------------\n")
    print(winner)
    text_file.write(winner)


















