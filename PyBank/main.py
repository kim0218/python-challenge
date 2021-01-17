#Import
import os
import csv

budget_data=os.path.join("Resources","budget_data.csv")
total_month=0
total_amount=0
change=0
change2=[]
previouse=0
average_change=0

with open(budget_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)
    print(header)
    
    for row in csvreader:
        total_month=total_month+1
        total_amount=total_amount+int(row[1])

        change=int(row[1])-previouse
        change2.append(change)
        previouse=int(row[1])

    average_change=sum(change2[1:])/len(change2[1:])
    great_increase=max(change2)
    great_decrease=min(change2)

      


    print("Total: $"+str(total_amount))
    print("Total Month: $"+str(total_month))
    print("Average Change: $"+str(average_change))
    print("Greatest Increase in Profits: $"+str(great_increase))
    print("Greatest Decrease in Profits: $"+str(great_decrease))


# Save result to txt
with open('Pybank.txt', 'w') as text_file:
    print("Total: $"+str(total_amount), file=text_file)
    print("Total Month: $"+str(total_month), file=text_file)
    print("Average Change: $"+str(average_change), file=text_file)
    print("Greatest Increase in Profits: $"+str(great_increase), file=text_file)
    print("Greatest Decrease in Profits: $"+str(great_decrease), file=text_file)