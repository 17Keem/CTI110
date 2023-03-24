Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # This project is used to calculate the travel expense. And it also formatted the output.
... # 3/9/23
... # CTI - 110 P2HW1 - Travel
... # Akeem Hall
... 
... 
... #code segment to take user input
... print("This program calculates and displays travel expenses")
... amount = int(input("Enter budget: "))
... dest = input("Enter your travel destination: ")
... gas = int(input("How much do you think you will spend on gas? "))
... hotel = int(input("Approximately, how much will you need for accommodation/hotel? "))
... food = int(input("Last, how much do you need for food? "))
... 
... #output
... print("---------------Travel Expense---------------")
... print(f"{'Location:' : <20}", f"{ dest : <20}")
... print(f"{'Initial budget:' : <20}", f"{ '$'+str(float(amount)) : <20}")
... print(f"{'Fuel:' : <20}", f"{'$'+str(float(gas)) : <20}")
... print(f"{'Accommodation:' : <20}", f" {'$'+str(float(hotel)) : <20}")
... print(f"{'Food:' : <20}", f"{'$'+str(float(food)) : <20}")
... 
... #calculating the remaining balance
... remaining = amount - (gas+hotel+food)
... print("--------------------------------------------")
... print(f"{'Remaining balance:' : <20}", f"{'$'+str(float(remaining)) : <20}")
