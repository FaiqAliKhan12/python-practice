# print(2)
# print(45.12)
# print(20*24*60)
# calculate_to_seconds = 24*60*60
# name_of_unit= "seconds"
# print("20 days are " +str(50)+ " minutes" )
# print("20 days are {50} minutes")
# print(f"20 days are  {20 * calculate_to_seconds} {name_of_unit}")
# print(f"20 days are  {35*24*60*60} seconds")
# print(f"20 days are  {110*24*60*60} seconds")

# hour_name = 24
# name = "hour"
# print(f"{20 * hour_name} {name}")

# encapsulate logic with function
calculate_to_hour = 24
name_of_unit= "hours"
def day_to_units(num_of_days,custome_message):
    print(f"{num_of_days} days are  {num_of_days * calculate_to_hour} {name_of_unit}")
    print(custome_message)


day_to_units(35,"Awesome!")
day_to_units(20,"Awesome!")
day_to_units(40,"Awesome!")
day_to_units(110,"Awesome!")
day_to_units(123,"Awesome!")