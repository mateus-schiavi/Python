import math
from datetime import datetime
running = True

def tire_volume_function(width_tire, aspect_tire, diameter_tire):
    return (math.pi * width_tire * width_tire * aspect_tire * (width_tire * aspect_tire + 2540 * diameter_tire)) / 10000000

print("Enter the width of the tire in mm:")
width_tire = int(input("--> "))
print("Enter the aspect ratio of the tire:")
aspect_tire = int(input("--> "))
print("Enter the diameter of the wheel in inches:")
diameter_tire = int(input("--> "))
 
volume = tire_volume_function(width_tire, aspect_tire, diameter_tire)
volume = round(volume, 1)
print(f"The approximate volume is {volume} milliliters.")

while running:
    shopping = input("Would you like to buy tires with these dimensions? (yes/no) ")
    if shopping.lower() == "y":
        print("Please enter a phone number, and we will contact you at a later time:")
        phone_number = input(">> ")
        print("Have a great day!")
        loop = False
    elif shopping.lower() == "n":
        print("Have a nice day!")
        phone_number = ("")
        loop = False
    else:
        print("Please enter Y/N.")

current_date_and_time = datetime.now()

with open("tire_volume.txt", "at") as dimension_main_file:
    print(f"\n{current_date_and_time}\n{width_tire}, {aspect_tire}, {diameter_tire}, {volume}\n{phone_number}", file=dimension_main_file)