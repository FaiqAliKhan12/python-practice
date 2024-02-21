def days_to(num_of_days,conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days*24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days*24*60} minutes"
    else: 
        return "unsupported unit"

def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_number= int(days_and_unit_dictionary["days"])
        if user_input_number>0:
            calculated_value= days_to(user_input_number,days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number ==0:
            print("You've entered 0 value, Enter valid value")
    except:
        print("your input is not a number , dont ruin program")

user_input_message = "Hey user, enter a number and conversion unit\n"