import random as rd
import math

print("""
select a mode:
(1) hypotenuse calc
more coming soon...""")
mode = input()
if mode == "1":
    print("base: ")
    b = float(input())
    print("height: ")
    h = float(input())
    print(f"hypotenuse: {math.hypot(b, h)}")
else:
    print("press the number next to the mode you want")

print("press enter to exit")
input()