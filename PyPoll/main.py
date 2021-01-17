#Import
import os
import csv

election_data=os.path.join("Resources","election_data.csv")

#List of store data
total_vote=0
candidates_list=[]
candidate=[]
total_percent=[]
total_count=[]
vote=[]
name=[]
khan_vote=0
khan_percent=0
corey_percent=0
corey_vote=0
li_vote=0
li_percent=0
otooley_vote=0
otooley_percent=0

# use encoding for Windows
#with open(election_data, newline=' ', encoding='utf-8') as csvfile:
with open(election_data, newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    next(csvreader)

# for loop
    for row in csvreader:
        #add total number of votes cast
        total_vote=total_vote+1


        
        #if row[2] not in candidates_list:
#candidates_list.append(row[2])

        #total_count.append(row[2])
        
        #add complete list of candidates who received votes
        #khan_vote = khan_vote+1 conditional loop
        if row[2]=="Khan":
            khan_vote+=1
        if row[2]=="Correy":
            corey_vote+=1
        if row[2]=="Li":
            li_vote+=1   
        if row[2]=="O'Tooley":
            otooley_vote+=1
    
                   
       #add percentage of votes each candidates  
        khan_percent=(khan_vote/total_vote)*1.00
        corey_percent=corey_vote/total_vote*1.00
        li_percent=li_vote/total_vote*1.00
        otooley_percent=otooley_vote/total_vote*1.00

    

# list of candidates names
# loop thorugh candidates_list
# if candidate = 'Khan', khan_vote = 0, khan_vote = khan_vote + 1

# print results
print("Election Results")
print("-------------------")

print("Total Votes: "+str(total_vote))
print("--------------------")

#for p in range(len(candidates_list)):
    #print(f'{candidates_list[p]}: {total_percent[p]}% {candidate[p]}')

print(f'Khan: {khan_percent:.3%} ({khan_vote})')
print(f'Correy: {corey_percent:.3%} ({corey_vote})')
print(f'Li: {li_percent:.3%} ({li_vote})')
print(f"O'Tooley: {otooley_percent:.3%} ({otooley_vote})")

print("--------------------")
print(f'Winner: Khan')
print(f"-------------------")

#save Analysis to txt
with open('PyPoll.txt', 'w') as text_file:
    print(f'Election Results', file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Total Votes: {total_vote}', file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Khan: {khan_percent:.3%} ({khan_vote})', file=text_file)
    print(f'Correy: {corey_percent:.3%} ({corey_vote})', file=text_file)
    print(f'Li: {li_percent:.3%} ({li_vote})', file=text_file)
    print(f"O'Tooley: {otooley_percent:.3%} ({otooley_vote})", file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Winner: Khan', file=text_file)
    print(f'-------------------------', file=text_file)