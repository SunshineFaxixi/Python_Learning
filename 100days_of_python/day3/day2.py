# print(round(8 / 3, 2))
# result = 4 / 2
# result /= 2
# print(result)

# score = 0
# height = 1.8
# isWining = True
# # f-string
# print(f"Your score is {score}, your height is {height}, your winning is {isWining}")

# age = Input("What is your current age?")
# age_as_int = int(age)
#
# years_remaining = 90- age_as_int
# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# month_remaining = years_remaining * 12
#
# print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {month_remaining} months to left")

total_bill = input("What was the total bill?")
percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15?")
num_of_person = input("How many people to split the bill?")
result = float(total_bill) * (1 + float(int(percentage_tip) / 100)) / int(num_of_person)
print(f"Each person should pay: ${result}")