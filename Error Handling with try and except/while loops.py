cal_to =24
name_to = "hour"
def days_to(num_of_days):
    return(f"{num_of_days} days are {num_of_days*cal_to}{name_to}")

def validate_and_execute():
    try:
        user_input_number= int(user_input)
        if user_input_number>0:
            calculated_value= days_to(user_input_number)
            print(calculated_value)
        elif user_input_number ==0:
            print("You've entered 0 value, Enter valid value")
    except:
        print("your input is not a number , dont ruin program")

user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter a number of days I convert it hours\n")
    validate_and_execute()  