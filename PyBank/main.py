#import library
import os
import csv

# CSV file to be read from Resources
csv_budget_data = os.path.join(".","Resources","budget_data.csv")

#Financial Analysis components
Total_Months = 0
Net_total_amount_profit_loss = 0.0
Average_change_profit_loss = 0.0
max_increase_in_profit = 0.0
max_decrease_in_profit = 0.0
monthly_profit_change = 0.0

# Read the CSV file
with open(csv_budget_data,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    

    for row in csvreader:
     
        #Calculating Total Months
        Total_Months = Total_Months + 1
        #Calculate Total Amount of Profit and Loss
        Net_total_amount_profit_loss = Net_total_amount_profit_loss + float(row[1])

    
        #Average Change
        if (Total_Months > 1):
            monthly_profit_change = float(row[1]) - Profit_last_month
            Average_change_profit_loss = Average_change_profit_loss +  monthly_profit_change 

        #Greatest increase in profits
        if (monthly_profit_change > max_increase_in_profit):
                max_increase_in_profit = monthly_profit_change
                max_increase_profit_month = row[0]    

        #Greatest decrease in profits
        if (monthly_profit_change < max_decrease_in_profit):
                max_decrease_in_profit = monthly_profit_change
                max_decrease_profit_month = row[0]    

        Profit_last_month = float(row[1])

Average_monthly_change = Average_change_profit_loss / (Total_Months - 1)

    #Printing the results
print(f"Financial Analysis")
print(f"-----------------------")
print(f"Total Months:{Total_Months}")
print(f"Total amount:${Net_total_amount_profit_loss}")
print(f"Average Change:${round(Average_monthly_change,2)}")
print(f"Greatest Increase in Profits:{max_increase_profit_month}(${max_increase_in_profit})")
print(f"Greatest Decrease in Profits:{max_decrease_profit_month}(${max_decrease_in_profit})")    

#Output the result to text file
Output_file = os.path.join("Analysis/budget_data.txt")

with open(Output_file, "w") as txtfile:
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"-----------------------\n")
    txtfile.write(f"Total Months:{Total_Months}\n")
    txtfile.write(f"Total amount:${Net_total_amount_profit_loss}\n")
    txtfile.write(f"Average Change:${round(Average_monthly_change,2)}\n")
    txtfile.write(f"Greatest Increase in Profits:{max_increase_profit_month}(${max_increase_in_profit})\n")
    txtfile.write(f"Greatest Decrease in Profits:{max_decrease_profit_month}(${max_decrease_in_profit})\n")
    





