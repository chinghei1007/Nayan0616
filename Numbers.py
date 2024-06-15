#https://nbviewer.org/github/jerry-git/learn-python3/blob/master/notebooks/beginner/exercises/02_numbers_exercise.ipynb

#If  you want to show that 0.1+0.2 == 0.3
from decimal import Decimal
import random
a = Decimal("0.1")
b = Decimal("0.2")

print(a+b)


r_n = random.randrange(1,5000,1)
guess = 0
""" while guess != r_n:
    guess = int(input("Please guess the number: "))
    if guess < r_n:
        print("larger!")
    if guess > r_n:
        print("smaller")
    else:
        print("Congrats!") """

import time

import time

num = 0
while True:
    print(f"\r The number is: {num}", end="")
    num += 1
    time.sleep(0.5)

