#!/usr/bin/env python
# coding: utf-8

# In[24]:


import os
import csv

file = os.path.join(".","Resources","election_data.csv")

file_output = os.path.join(".","analysis","election_winner.txt")

with open(file) as election_file:
    file_reader = csv.reader(election_file, delimiter = ",")
    
    header = next(file_reader)
    total = 0
    total_charles = 0
    total_diana = 0
    total_raymon = 0
    
    for row in file_reader:
        if row[2] == "Charles Casper Stockham":
            total_charles+=1
        if row[2] == "Diana DeGette":
            total_diana+=1
        if row[2] == "Raymon Anthony Doane":
            total_raymon+=1
        total +=1
        
    most_votes = max(total_charles,total_diana,total_raymon)
    
    if most_votes == total_charles:
        winner ="Charles Casper Stockham"
    elif most_votes == total_diana:
        winner = "Diana DeGette"
    else:
        winner = "Raymon Anthony Doane"
output = ( f'Election Results\n'
           f'-------------------------\n'
           f'Total Votes: {total}\n'
           f'-------------------------\n'
           f'Charles Casper Stockham: {round(total_charles/total *100,3)}% ({total_charles})\n'
           f'Diana DeGette: {round(total_diana/total *100,3)}% ({total_diana})\n'
           f'Raymon Anthony Doane: {round(total_raymon/total *100,3)}%({total_raymon})\n'
           f'-------------------------\n'
           f'Winner: {winner}\n'
           f'-------------------------\n')
print(output)

with open(file_output, 'w') as election_winner:
    election_winner.write(output)


# In[ ]:




