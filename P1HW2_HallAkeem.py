Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>>     # This program calculates and displays the travel expenses and remaining balance
...     # 03/09/23
...     # CTI-110 P1HW2 - Travel Expense
...     # Akeem Hall
... print("This program calculates and displays travel expenses")
... budget = float(input("Enter your budget : "))   # reading user budget
... destination = input("Enter your destination : ")    # reading user destination
... gas_expenses = float(input("How much you will spend on gas : "))    # reading user fuel expenses
... accomodation = float(input("Approximately how much you need for accomodation ? : "))    # reading user hostel expenses
... food_expenses = float(input("Last, how much do you need for food? : "))     # reading user food expenses
... remaining_balance = budget - gas_expenses - accomodation - food_expenses    # calculating remaining balance
... print("------------------------------travel expenses----------------------------------")
... print("Location : " + destination)
... print("Initial budget : " + str(budget))
... print()
... print("Fuel : " + str(gas_expenses))
... print("Accomodation : " + str(accomodation))
... print("Food : " + str(food_expenses))
... print()
