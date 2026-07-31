running_total = 0

num_of_friends = int(input("Enter the number of people: "))
if num_of_friends <= 0:
    print("Number of people must be greater than 0.")
else:    
    appetizers = float(input("Enter the total cost of appetizers: "))

    main_courses = float(input("Enter the total cost of main courses: "))

    desserts = float(input("Enter the total cost of desserts: "))

    drinks = float(input("Enter the total cost of drinks: "))

    running_total += appetizers + main_courses + desserts + drinks
    print(f"Total bill so far: ₦{running_total:.2f}")

    tip_percentage = float(input('Enter the tip percentage(%): '))
    tip_percentage = tip_percentage / 100

    tip = running_total * tip_percentage
    print(f"Tip amount: ₦{tip:.2f}")

    running_total += tip
    print(f"Total with tip: ₦{running_total:.2f}")

    final_bill = running_total / num_of_friends
    print(f"Bill per person: ₦{final_bill:.2f}")