# Calculates the amount of money made by each employee
# 2/16/23
# CTI-110 P1HW2 - Travel Expense
# Akeem Hall
employeeName = input( "Enter Name: \n")
hourRate = int(input("Enter hourly Rate: \n"))
hrsWorked = int(input( "Enter hours worked: \n"))
total = hourRate*hrsWorked

print("\nEmployee Name: ", employeeName, "\nhourly Rate: " ,hourRate, "\nHours Work: ", hrsWorked, "\nTotal Earned: $" , total)