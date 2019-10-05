
import os
import csv

csvpath = os.path.join("C:\\Users\\irais\\OneDrive\\Desktop\\python-challenge\\PyPoll\\election_data.csv")


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

