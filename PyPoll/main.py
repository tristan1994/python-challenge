import os

# Module for reading csv file
import csv
#Input path
csvpath = os.path.join('Resources', 'election_data.csv')

#Output path
result = os.path.join('analysis', 'analysis.txt')

vote = []
candidate = []
vote_percent=[]
total_vote = 0


with open(csvpath) as csvfile:
    #CSV reader specifies delimiter and variable that hold contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #Reader the header row first(skip the header to go straight to the data set)
    csv_header = next(csvreader)

    
    for row in csvreader:
        total_vote = total_vote+1
        

        if row[2] not in candidate:
            candidate.append(row[2])
            index = candidate.index(row[2])
            vote.append(1)
        else:
            index = candidate.index(row[2])
            vote[index] += 1

    for x in vote:
        percentage = round((x/total_vote)*100, 2)
        vote_percent.append(percentage)

    winner = max(vote)
    index = vote.index(winner)
    won_candidate = candidate[index]
    

print("Election Results")
print("---------------------")
print(f'Total Vote: {total_vote}')
print("---------------------")
for i in range(len(candidate)):
    print(f'{candidate[i]}: {vote_percent[i]}% ({vote[i]})')
print("---------------------")
print(f'Winner: {won_candidate}')
print("---------------------")     
   


with open(result, 'w') as text_file:
    text_file.write("Election Results")
    text_file.write("\n")
    text_file.write("---------------------")
    text_file.write("\n")
    text_file.write(f'Total Vote: {total_vote}')
    text_file.write("\n")
    text_file.write("---------------------")
    text_file.write("\n")
    for i in range(len(candidate)):
        text_file.write(f'{candidate[i]}: {vote_percent[i]}% ({vote[i]})')
    text_file.write("\n")    
    text_file.write("---------------------")
    text_file.write("\n")
    text_file.write(f'Winner: {won_candidate}')
    text_file.write("\n")
    text_file.write("---------------------")