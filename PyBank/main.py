
import os
import csv

csvpath = os.path.join("C:\\Users\\irais\\OneDrive\\Desktop\\Resources\\budget_data.csv")

total_months_l = []
total_l = []
avg_change_l = []


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    print(csvreader)

    for row in csvreader:
        
        total_months_l.append(row[0])

        total_l.append(int(row[1]))

    for i in range(len(total_l)-1):
        
        avg_change_l.append(int(total_l[i+1])-int(total_l[i]))
        avg_change_sum = sum(avg_change_l)
        avg_change_count = len(avg_change_l)
    
   
    total_months = len(total_months_l)
    total = sum(total_l)
    avg_change = avg_change_sum/avg_change_count

    max_increase = max(avg_change_l)
    min_increase = min(avg_change_l)

    max_increase_month = total_months_l[avg_change_l.index(max_increase)+1]
    min_increase_month = total_months_l[avg_change_l.index(min_increase)+1]


    print(str(total_months))
    print(str(total))
    print(str(avg_change))
    print(max_increase)
    print(min_increase)
    print(max_increase_month)
    print(min_increase_month)
