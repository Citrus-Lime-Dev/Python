#Explicit Conversion of Data types
print(int(True)) -> 1
print(int(False)) -> 0
print(int(2.56)) -> 2
print(int("143")) -> 143
# print(int("abc")) -> Produces error 

print(float(2)) -> 2.0
print(float(True)) -> 1.0
print(float("123")) -> 123.0
# print(float("abc")) -> Produces error 

print(str(12345)) -> "12345"
print(str(True)) -> "True"
print(str(2.56)) -> "2.56"

print(bool(123)) -> True
print(bool("")) -> False
print(bool(" ")) -> True
print(bool("abc")) -> True
