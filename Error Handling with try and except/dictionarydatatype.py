# cal_to =24
# name_to = "hour"
def days_to(num_of_days,conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days*24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days*24*60} minutes"
    else: 
        return "unsupported unit"

def validate_and_execute():
    try:
        user_input_number= int(days_and_unit_dictionary["days"])
        if user_input_number>0:
            calculated_value= days_to(user_input_number,days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number ==0:
            print("You've entered 0 value, Enter valid value")
    except:
        print("your input is not a number , dont ruin program")

user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter a number and conversion unit\n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0],"unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_execute()


message = "enter value"
days = 20
price = 9.99
valid_number = True
exit_input = False
list_of_days = [20,40,20,100]
list_of_months = ["January","February","June"]
set_of_days = {20,45,60}
days_and_unit = {"days":10,"unit":"hours"}
"""my_list = ["20","30","100"]
print(my_list[2])

my_dictionary = {"days":20, "unit":"hours","message":"all good"}
print(my_dictionary["message"])"""