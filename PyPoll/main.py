#Import modules
import os
import csv

#Declare and initialize variables
totalVotes = 0
votesKhan = 0
votesCorrey = 0
votesLi = 0
votesOTooley = 0
percentKhan = 0
percentCorrey = 0
percentLi = 0
percentOTooley = 0
winner = ""

#Locate election data file
electionData = os.path.join('Resources', 'election_data.csv')

#Read CSV
with open(electionData) as csvfile:

    electionReader = csv.reader(csvfile, delimiter=",")

    next(electionReader)

    for row in electionReader:

        #Counts each row as a vote
        totalVotes += 1

        #If statements determine which candidate gets a vote
        if row[2] == "Khan":
        
            votesKhan += 1

        elif row[2] == "Correy":

            votesCorrey += 1

        elif row[2] == "Li":

            votesLi += 1

        elif row[2] == "O'Tooley":

            votesOTooley += 1

#Calculates a candidate's percentage of the vote and rounds it
percentKhan = (votesKhan/totalVotes) * 100
percentKhan = round(percentKhan, 2)

percentCorrey = (votesCorrey/totalVotes) * 100
percentCorrey = round(percentCorrey, 2)

percentLi = (votesLi/totalVotes) * 100
percentLi = round(percentLi, 2)

percentOTooley = (votesOTooley/totalVotes) * 100
percentOTooley = round(percentOTooley, 2)

#Determines the winner of the election
if votesKhan > votesCorrey and votesKhan > votesLi and votesKhan > votesOTooley:
    
    winner = "Khan"

elif votesCorrey > votesKhan and votesCorrey > votesLi and votesCorrey > votesOTooley:

    winner = "Correy"

elif votesLi > votesKhan and votesLi > votesCorrey and votesLi > votesOTooley:

    winner = "Li"

else:

    winner = "O'Tooley"


#Writes results into a .txt file
f = open("Analysis/election_results.txt", "x")
f.write(f'Election results \n')
f.write(f'------------------------------------------ \n')
f.write(f'Total votes: {totalVotes} \n')
f.write(f'------------------------------------------ \n')
f.write(f'Khan: {percentKhan}% ({votesKhan}) \n')
f.write(f'Correy: {percentCorrey}% ({votesCorrey}) \n')
f.write(f'Li: {percentLi}% ({votesLi}) \n')
f.write(f"O'Tooley: {percentOTooley}% ({votesOTooley}) \n")
f.write(f'------------------------------------------ \n')
f.write(f'Winner: {winner} \n')
f.close

#Writes results into console
print(f'Election results')
print(f'------------------------------------------')
print(f'Total votes: {totalVotes}')
print(f'------------------------------------------')
print(f'Khan: {percentKhan}% ({votesKhan})')
print(f'Correy: {percentCorrey}% ({votesCorrey})')
print(f'Li: {percentLi}% ({votesLi})')
print(f"O'Tooley: {percentOTooley}% ({votesOTooley})")
print(f'------------------------------------------')
print(f'Winner: {winner}')
