cal_to =24
name_to = "hour"
def days_to(num_of_days):
    return(f"{num_of_days} days are {num_of_days*cal_to}{name_to}")

def validate_and_execute():
    try:
        user_input_number= int(num_of_days_element)
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
    list_of_days = user_input.split(",")
    
    print(list_of_days)
    print(set(list_of_days))

    print(type(list_of_days))
    print(type(set(list_of_days)))
    
    # print(set(user_input.split(",")))
    for num_of_days_element in set(user_input.split(",")):
        validate_and_execute()
