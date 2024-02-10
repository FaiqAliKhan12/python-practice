cal_to = 24
name_to = "hour"



def days_to(num_of_days):
    return(f"{num_of_days} days are {num_of_days * cal_to} {name_to}")

# my_var = days_to(20)
# print(my_var)



# input("Hey user, enter a number of days and I will convert it to hours!\n")
user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
user_input_number = int(user_input)
calculated_value = days_to(user_input_number)
print(calculated_value)