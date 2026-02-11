# Blood Donation Eligibility using Nested if
age= int(input("Enter your age:"))
Weight= float(input("Enter weight (kg):"))

if age >= 18:
    if Weight >=50:
        print("Eligible for blood donation")
    else:
        print("Not eligible, weight is less then 50")

else:
    print("Not eligible, your age is less")