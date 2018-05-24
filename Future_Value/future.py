#!/usr/bin/env python3
print("Welcome To The Future Value CalCulator ")
print("=======================================")

# variable 
choice = "y"
while choice.lower() == "y":
    monthly_investment = float(input("Enter The Monthly Investment Rate: "))
    yearly_investment_rate = float(input("Enter The Yearly Interest Rate:\t"))
    years = int(input("Enter The Number Of Years: "))

    monthly_interest_rate = yearly_investment_rate / 12 /100
    months = years * 12

    # calculate the future value 
    future = 0
    for i in range(months):
        future += monthly_investment
        monthly_investment_amount = future * monthly_interest_rate
        future += monthly_investment_amount

        # print the results here 
    print("The Future Value:\t\t", str(round(future, 2)))
    print()
    choice = input("Continue (y/n)\t")
    if choice.lower() == "n":
        print("Good Bye Keep IN Touch Guys")
    else:
        print()   



