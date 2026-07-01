import math # Imported math module for floor and ceil functions to work

bmi = 84 / 1.65 ** 2
print(bmi) # 30.85399449035813

print(int(bmi)) # Implicit conversion to lower value so , 30

print(round(bmi)) # Conversion according to the decimal value , 31 if > 0.5, 30 if < 0.5

print(round(bmi, 2)) # Rounds to 2 places -> 30.85

print(math.floor(bmi)) # 30
print(math.ceil(bmi)) # 31
