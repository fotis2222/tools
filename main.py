import random as rd
import math

print("""
select a mode:
(1) hypotenuse calc
(2) dice roller
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
else:
    print("press the number next to the mode you want")

#exit sequence
print("press enter to exit")
input()