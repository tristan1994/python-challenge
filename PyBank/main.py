# Allow to create file paths across operating system
import os

# Module for reading csv file
import csv
#Input path
csvpath = os.path.join('Resources', 'budget_data.csv')

#Output path
result = os.path.join('analysis', 'analysis.txt')

#Setting variable and store it as list
#Total number of months included in the dataset
month = []

#The net total amount of "Profit/Losses" over the entire period
profit = []

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
monthly_profit_change = []
average_net = 0
#The greatest increase in profits (date and amount) over the entire period
greatest_inc = 0

#The greatest decrease in losses (date and amount) over the entire period
greatest_dec = 0



with open(csvpath) as csvfile:
    #CSV reader specifies delimiter and variable that hold contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #Reader the header row first(skip the header to go straight to the data set)
    csv_header = next(csvreader)

    for row in csvreader:
        month.append(row[0])
        profit.append(int(row[1]))


    for i in range(len(profit)-1):
        monthly_profit_change.append(profit[i+1]-profit[i])


total_months = len(month)
total_profits = sum(profit)
average_net = round(sum(monthly_profit_change)/len(monthly_profit_change),2)
greatest_inc = max(monthly_profit_change)
greatest_dec = min(monthly_profit_change)

max_month = monthly_profit_change.index(max(monthly_profit_change))+1
min_month = monthly_profit_change.index(min(monthly_profit_change))+1

print("Financial Analysis")
print("--------------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${total_profits}')
print(f'Average Change: ${average_net}')
print(f'Greatest Increase in Profits: {month[max_month]} (${greatest_inc})')
print(f'Greatest Decrease in Profits: {month[min_month]} (${greatest_dec})')

with open(result, 'w') as text_file:
    text_file.write("Financial Analysis")
    text_file.write("\n")
    text_file.write("--------------------------------")
    text_file.write("\n")
    text_file.write(f'Total Months: {total_months}')
    text_file.write("\n")
    text_file.write(f'Total: ${total_profits}')
    text_file.write("\n")
    text_file.write(f'Average Change: ${average_net}')
    text_file.write("\n")
    text_file.write(f'Greatest Increase in Profits: {month[max_month]} (${greatest_inc})')
    text_file.write("\n")
    text_file.write(f'Greatest Decrease in Profits: {month[min_month]} (${greatest_dec})')
