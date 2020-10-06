#import library
import os
import csv

# CSV file to be read from Resources
csv_election_data = os.path.join(".","Resources","election_data.csv")

#List of variables
Total_votes = 0
Khan_vote = 0
Correy_vote = 0
Li_vote = 0
Otooley_vote = 0

# Read the CSV file
with open(csv_election_data,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    

    for row in csvreader:
     
        #Calculating Total Votes
        Total_votes = Total_votes + 1

        #Calculating candidate votes
        if (row[2] == "Khan"):
            Khan_vote = Khan_vote + 1
        elif (row[2] == "Correy"):
            Correy_vote = Correy_vote + 1
        elif (row[2] == "Li"):
            Li_vote = Li_vote + 1
        else:
            Otooley_vote = Otooley_vote + 1        

        #Calculating percentage of voters for each candidate
        Khan_percent = Khan_vote / Total_votes
        Correy_percent = Correy_vote / Total_votes
        Li_percent = Li_vote / Total_votes
        Otooley_percent = Otooley_vote / Total_votes

        #Calculating maximum number of votes each candidate won to analyze the winner
        maximum_votes = max(Khan_vote, Correy_vote, Li_vote, Otooley_vote)

        if maximum_votes == Khan_vote:
            winner = "Khan"

        elif maximum_votes == Correy_vote:
            winner = "Correy"

        elif maximum_votes == Li_vote:
            winner = "Li"

        else:
            winner = "Otooley"    


        

    #Printing the results
print(f"Election results")
print(f"-----------------------")
print(f"Total votes:{Total_votes}")
print(f"-----------------------")
print(f"Khan: {round((Khan_percent*100), 3)}% ({Khan_vote})")
print(f"Correy: {round((Correy_percent*100),3)}% ({Correy_vote})")
print(f"Li: {round((Li_percent*100),3)}% ({Li_vote})")
print(f"O'Tooley: {round((Otooley_percent*100),3)}% ({Otooley_vote})")
print(f"-----------------------")
print(f"Winner:{winner}")
print(f"-----------------------")
  
#Output the result to text file
Output_file = os.path.join("Analysis/election_data.txt")

with open(Output_file, "w") as txtfile:
    txtfile.write(f"Election results\n")
    txtfile.write(f"-----------------------\n")
    txtfile.write(f"Total votes:{Total_votes}\n")
    txtfile.write(f"-----------------------\n")
    txtfile.write(f"Khan: {round((Khan_percent*100), 3)}% ({Khan_vote})\n")
    txtfile.write(f"Correy: {round((Correy_percent*100),3)}% ({Correy_vote})\n")
    txtfile.write(f"Li: {round((Li_percent*100),3)}% ({Li_vote})\n")
    txtfile.write(f"O'Tooley: {round((Otooley_percent*100),3)}% ({Otooley_vote})\n")
    txtfile.write(f"-----------------------\n")
    txtfile.write(f"Winner:{winner}\n")
    txtfile.write(f"-----------------------\n")
