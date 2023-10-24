import csv


total_months = 0
net_total = 0
previous_profit_loss = None
total_profit_loss_change = 0
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""

file_path = 'Resources/budget_data.csv'
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    csv_data = list(reader)
    # [ ['Date', 'Profit/Losses'], ['1/1/2012', '1000000'] ]
    csv_data = csv_data[1:]

    for row in csv_data:
        date = row[0]
        profit_loss = row[1]
        profit_loss = int(profit_loss)

        total_months = total_months + 1
        net_total = net_total + profit_loss

        if previous_profit_loss is not None:
            profit_loss_change = profit_loss - previous_profit_loss
            total_profit_loss_change = total_profit_loss_change + profit_loss_change

            if profit_loss_change > greatest_increase:
                greatest_increase = profit_loss_change
                greatest_increase_month = date

            if profit_loss_change < greatest_decrease:
                greatest_decrease = profit_loss_change
                greatest_decrease_month = date

        previous_profit_loss = profit_loss

average_change = total_profit_loss_change / (total_months - 1)
average_change = round(average_change, 2)

# Print the analysis
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

with open('analysis/financial_analysis.txt', 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_change}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")

