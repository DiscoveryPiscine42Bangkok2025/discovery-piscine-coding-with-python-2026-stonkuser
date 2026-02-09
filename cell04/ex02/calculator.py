#!/usr/bin/env python3

a = int(input("Give me the first number: "))
b = int(input("Give me the second number: "))

print("Thank you!")

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} / {b} = {a // b if a % b == 0 else a / b}")
print(f"{a} * {b} = {a * b}")
