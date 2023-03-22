#Mateus Schiavi
#CSE 111
#01 Prove Milestone

import math
 
from datetime import datetime

running = True;

print("Welcome to Tire Volume Calculator")
print("|:|:|:|:|:|:|:|:|:|:|:|:|:|:|:|:|")

def main():
    width = int(input("Enter the width of the tire in mm: "))
    respective_ratio = int(input("Enter the aspect ratio of the tire: "))
    respective_diameter = int(input("Enter the diameter of the wheel in inches: "))

    volume = round(((math.pi * width ** 2 * respective_ratio * (width * aspect_ratio + 2540 * respective_diameter)) / 10000000), 1)

    print(f"The respective volume is {volume} milliliters.")
    repeat()

def repeat():
    answer = input("Would you like to compute another volume (Y/N)? ")
    if answer.upper() == "Y":
        main()
    if answer.upper() == "N":
        print("The program will now end")
        exit()
    else:
        print("Error: Invalid Argument")
        repeat()

while running:
    shopping = input("Would you like to buy tires with these dimensions? (yes/no) ")
    if shopping.lower() == "yes":
        print("Please enter a phone number, and we will contact you at a later time:")
        phone_number = input(">> ")
        print("Have a great day!")
        loop = True
    elif shopping.lower() == "no":
        print("Have a great day!")
        phone_number = ("")
        loop = False
    else:
        print("Please enter yes or no.")

current_date_and_time = datetime.now()

with open("tire_volume.txt", "at") as dimens_file:
    print(f"\n{current_date_and_time}\n{width_tire}, {aspect_tire}, {diameter_tire}, {volume}\n{phone_number}", file=dimens_file)
main()
