"""
String formatting
"""

name = "Gönül"
surname = "Polat"
age = 18

# 1. Using % operator

print("Hello, my name is %s %s. I'am %d years old." % (name, surname, age))

# 2. Using format() method

print("Hello, my name is {} {}. I'am {} years old.".format(name, surname, age))

# 3. Using f-string

print(f"Hello, my name is {name} {surname}. I'am {age} years old.")

# 4. Using string concatenation

print("Hello, my name is " + name + " " + surname + ". I'am " + str(age) + " years old.")

# 5. Using join() method

print("Hello, my name is " + " ".join([name, surname]) + ". I'am " + str(age) + " years old.")

# 6. Using string interpolation

print("Hello, my name is {0} {1}. I'am {2} years old.".format(name, surname, age))

# 7. Using string interpolation with named arguments

print("Hello, my name is {n} {s}. I'am {a} years old.".format(n=name, s=surname, a=age))



