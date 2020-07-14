#Your task is to create a Python script that analyzes the records to calculate each of the following:
#Import dependencies



import os
import csv
months = []
total = []
profit = []
difference = []
greatest_increase = []
greatest_decrease = []


with open ('budget_data.csv','r') as f:
    reader = csv.DictReader(f, delimiter=',')

    for row in reader:
        months.append(row["Date"])
        total.append(int(row["Profit/Losses"]))
#The net total amount of "Profit/Losses" over the entire period
with open('PyBank.txt', "w")as txt_file:
    total_months = f"Total Months: {len(months)}"
    print(total_months)
    txt_file.write(total_months)
    total_profit = f"\nTotal: ${sum(total)}"
    print(total_profit)
    txt_file.write(total_profit)
#The average of the changes in "Profit/Losses" over the entire period
    for i in range(1, len(total)):
        difference.append(total[i] - total[i-1])
    
    average_change = round(sum(difference)/(len(months)-1), 2)
    change = f"\nAverage Change: ${average_change}"
    print(change)
    txt_file.write(change)
    greatest_increase = max(difference)
    greatest_decrease = min(difference)
    #The greatest increase in profits (date and amount) over the entire period
    greatest_increase_month = str(
        months[difference.index(greatest_increase)+1])
    #The greatest decrease in losses (date and amount) over the entire period
    greatest_decrease_month = str(
        months[difference.index(greatest_decrease)+1])

    increase = f"\nGreatest Increase in Profits: {greatest_increase_month} (${greatest_increase})"
    print(increase)
    txt_file.write(increase)
    decrease = f"\nGreatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})"
    print(decrease)
    txt_file.write(decrease)

   
    
   
   




















#Read in CSV file




