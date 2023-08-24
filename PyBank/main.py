#!/usr/bin/env python
# coding: utf-8

# In[38]:


import os
import csv
import statistics

file = os.path.join(".","Resources","budget_data.csv")

file_output = os.path.join(".","analysis","budget_analysis.txt")

net_change = []


with open(file, 'r') as financial_data:
    data_reader = csv.reader(financial_data, delimiter=',')
    
    header = next(data_reader)
    
    first_row = next(data_reader)
    previous_net = int(first_row[1])
    total = int(first_row[1])
    min_value = 0
    max_value = 0
    
    total_month =0
    
    for row in data_reader:
        difference  = 0
        total += int(row[1])
        difference = int(row[1])- previous_net
        net_change.append(difference)
        
        if difference > max_value:
            max_value = difference
            increase_profit = ( f"{row[0]} {max_value}")
            
        if difference < min_value:
            min_value = difference
            decrease_profit = ( f"{row[0]} {min_value}")
        previous_net = int(row[1])
        
        total_month +=1

    average_change = round(statistics.mean(net_change),2)
    
output = (f'Financial Analysis\n'
          f'----------------------------\n'
          f'Total Months {total_month}\n'
          f'Total: {total}\n'
          f'Average Change: {average_change}\n'
          f'Greatest Increase in Profits: {increase_profit}\n'
          f'Greatest Decrease in Profits: {decrease_profit}\n')
print(output)
    
with open(file_output, 'w') as txt_file:
    txt_file.write(output)



# In[ ]:




