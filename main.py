import random as rd
import math
import datetime as dt

print("""
select a mode:
(1) hypotenuse calc
(2) dice roller
(3) current date and time (for some reason, YY-MM-DD)
(4) calculator
(5) tip calculator
(6) converter
more coming soon...""")
mode = input()
if mode == "1":
    print("base: ")
    b = float(input())
    print("height: ")
    h = float(input())
    print(f"hypotenuse: {math.hypot(b, h)}")
elif mode == "2":
    print("sides of dice: ")
    sides = int(input())
    print(f"you rolled a: {rd.randint(1, sides)}")
elif mode == "3":
    print(dt.datetime.now())
elif mode == "4":
    print("select first number")
    a = float(input())
    print("select second number")
    b = float(input())
    print("""
select operation:
(1) +
(2) -
(3) *
(4) /
dont forget to have inputed the numbers in right order and select the number next to the operation
type quit to quit""")
    operation = input()
    if operation.lower() != "quit":
        if operation == "1":
            print(f"result: {a + b}")
        elif operation == "2":
            print(f"result: {a - b}")
        elif operation == "3":
            print(f"result: {a * b}")
        elif operation == "4":
            print(f"result: {a / b}")
        else:
            print("""
ENTER THE NUMBER NEXT TO THE OPERATION WHAT DO YOU NOT UNDERSTAND
uhh sowwy OwO""")
elif mode == "5":
    print("how much did it cost")
    cost = float(input())
    print("% of tip")
    percent = float(input())
    tip = (cost * (percent / 100))
    print(f"tip an extra ${tip}")
elif mode == "6":
    print("""
convert:
(1) kg to lbs
(2) lbs to kg
more coming soon...""")
    conversion = input()
    if conversion == "1":
        print("how many kgs:")
        kg = float(input())
        print(f"~{kg * 2.2} lbs")
    elif conversion == "2":
        print("how many lbs:")
        lbs = float(input())
        print(f"~{lbs / 2.2} kg")
    else:
        print("the number next to the conversionnnnnnnnnnnnnnn")
else:
    print("press the number next to the mode you want")

#exit sequence
print("press enter to exit")
input()