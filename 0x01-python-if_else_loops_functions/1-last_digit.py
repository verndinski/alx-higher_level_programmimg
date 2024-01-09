#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10

message = f"last digit of {number} is {lastdigit} "
if lastdigit > 5:
    message += "and is greater than 5"
elif lastdigit < 6 and lastdigit != 0:
    message += "and is less than 6 and not 0"
else:
    message += "and is 0"

print(message)
