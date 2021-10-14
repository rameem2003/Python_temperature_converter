#############################################
#                                           #
#  Python temperature converter system by   #
#          Mahmood Hassan Rameem            #
#                                           #
#############################################

import time
# Banner
print("#############################################")
print("#                                           #")
print("#  Python temperature converter system by   #")
print("#          Mahmood Hassan Rameem            #")
print("#                                           #")
print("#############################################")

time.sleep(2)
# Start main programme
print("Let's start!")
print("choose your's option. ")
print("1. Celsius to Fahrenheit.")
print("2. Fahrenheit to Celsius.")

op = int(input("What's your choice?(1 or 2): "))

if op == 1:
    print("Ok you choose 'Celsius to Fahrenheit.' ")
    c = float(input("Enter the value of Celsius temperature: "))
    f = (9*c + 160)/5
    print("The Fahrenheit value is", f, "F")

elif op == 2:
    print("Ok you choose 'Fahrenheit to Celsius.' ")
    f = float(input("Enter the value of Fahrenheit temperature: "))
    c = (5*f - 160)/9
    print("The Celsius value is", c, "C")
else:
    print("Wrong value input")




