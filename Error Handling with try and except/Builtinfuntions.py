cal_to = 24
name_to = "hour"
def days_to(num_of_days):
        return(f"{num_of_days} days are {num_of_days * cal_to} {name_to}")
   
def validate_and_execute():
    try:
    # if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number>0:
            calculated_value = days_to(user_input_number)
            print(calculated_value)
        elif user_input_number == 0 :
            print("You've Entererd 0 Value, Enter a valid value")      
    except ValueError:
            print("Your input is not number. Dont ruin my program")

user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
validate_and_execute()

# Builtin functions
print("some text")
input("enter value")
set([1,3,4])
int("20")
# directly value calling function
"2,3".split()
"text".isdigit()
[2,3,4].count()