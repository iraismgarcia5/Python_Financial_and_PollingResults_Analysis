
import os
import csv

csvpath = os.path.join("C:\\Users\\irais\\OneDrive\\Desktop\\Resources\\election_data.csv")


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

