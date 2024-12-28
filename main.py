import math
from datetime import datetime as dt



# how many function are there in math module
# print(dir(math))

# print(len(dir(math)))

# print(math.pi)

# calculate the remainder after dividing 4569 by 32
# print(math.remainder(4569,2))

# round up this value : 30.3

# value = 30.3
# print(f"the ceiling value of {value} is {math.ceil(value)}")
# print(f"the floor value of {value} is {math.floor(value)}")


print(dt.today())
print(dt.now())
print(dt.now().strftime('%Y-%m-%d %H,%M,%S'))
print(dt.now().hour)


def get_CT():
    current_time