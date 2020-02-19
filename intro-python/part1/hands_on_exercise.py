"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi

print("pi on {} jonka arvo on  {}".format(type(pi), pi))

# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if i < 50:
    print("i is less than 50")
elif i > 50:
    print("i is greater than 50")
else:
    print("yksi sadasta")

# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])

if picked_fruit == 'orange':
    print("Hedelmä on oranssi")
elif picked_fruit == 'strawberry':
    print("Hedelmä on punainen")
elif picked_fruit == 'banana':
    print("Hedelmä on keltainen")


# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def kertoja(num1, num2):
    result = num1 * num2
    return result


# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =", kertoja(12, 96))

print("48 x 17 =", kertoja(48, 17))

print("196523 x 87323 =", kertoja(196523, 87323))
