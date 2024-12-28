import math

# how many function are there in math module
print(dir(math))

print(len(dir(math)))

print(math.pi)

# calculate the remainder after dividing 4569 by 32
# print(math.remainder(4569,2))

# round up this value : 30.3

value = 30.3
print(f"the ceiling value of {value} is {math.ceil(value)}")
print(f"the floor value of {value} is {math.floor(value)}")
