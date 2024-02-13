#################################################################################
#
#  Purpose: This appliccation is a way to mix and match colors: blue, red and yellow. Dependoing on the two chosen colors, a new color will be generated. 
#  Developer: Darien Salazar
#  Coded on: 2-9-24
#  Version: 1.0.0
#
#################################################################################

RED = "red"
BLUE = "blue"
YELLOW = "yellow"

userName = input("Hello, what is your name?\n")
print(f"Nice to meet you {userName}, let's mix some colors!")
color1 = input(f"Okay {userName}, let's pick our first color. What color would you like to pick?\n")

if color1.lower() == BLUE or color1.lower() == RED or color1.lower() == YELLOW:
    color2 = input(f"Awesome! You've picked {color1}. Now we need a second color, choose a second color {userName}.\n")
    
    if color2.lower() == BLUE or color2.lower() == RED or color2.lower() == YELLOW:
        if (color1.lower() == RED and color2.lower() == BLUE) or (color1.lower() == BLUE and color2.lower() == RED):
            print(f"When you mix {color1} and {color2} you get PURPLE")
        elif (color1.lower() == RED and color2.lower() == YELLOW) or (color1.lower() == YELLOW and color2.lower() == RED):
            print(f"When you mix {color1} and {color2} you get ORANGE")
        elif (color1.lower() == BLUE and color2.lower() == YELLOW) or (color1.lower() == YELLOW and color2.lower() == BLUE):
            print(f"When you mix {color1} and {color2} you get GREEN")
    else:
        print("Oh no, that color is not one of the options. Let's try again.\n")
else:
       print("You must pick between yellow, red or blue, let's try again")