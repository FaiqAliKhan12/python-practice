cal_to = 24
name_to = "hour"
def days_to(num_of_days):
    # print(num_of_days>0)
    # condition_check = num_of_days>0
    # print(type(condition_check))
    if num_of_days>0:
        return(f"{num_of_days} days are {num_of_days * cal_to} {name_to}")
    elif num_of_days == 0:
        return "You've Entererd 0 Value, Enter a valid value"
    else:
        return "You Entered invalid value"
# my_var = days_to(20)
# print(my_var)
# input("Hey user, enter a number of days and I will convert it to hours!\n")
def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        calculated_value = days_to(user_input_number)
        print(calculated_value)
    else:
        print("Your input is not number. Dont ruin my program")

user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
validate_and_execute()