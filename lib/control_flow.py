#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
    

def hows_the_weather(temperature):
     if temperature < 40:
        return "It's brisk out there!"
     elif 40 <= temperature <= 65:
        return "It's a little chilly out there!"
     elif temperature > 85:
        return "It's too dang hot out there!"
     else:
        return "It's perfect out there!"

def fizzbuzz(number):
   if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
   elif number % 3 == 0:
        return "Fizz"
   elif number % 5 == 0:
        return "Buzz"
   else:
        return number
def calculator(operation, num1, num2):
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }
    if operation not in ops:
        print("Invalid operation!")
        return None
    return ops[operation](num1, num2)
calculator("+", 1, 1)
admin_login("sudo", "12345")
# "Access denied"
admin_login("admin", "12345")
# "Access granted"
admin_login("ADMIN", "12345")
# "Access granted"
hows_the_weather(33)
# "Brisk!"
hows_the_weather(99)
# "Too dang hot"
hows_the_weather(75)
# "Perfect!"
fizzbuzz(1)
# 1
fizzbuzz(2)
# 2
fizzbuzz(3)
# Fizz
fizzbuzz(4)
# 4
fizzbuzz(5)
# Buzz
fizzbuzz(15)
# FizzBuzz
calculator("+", 1, 1)
# 2
calculator("-", 3, 1)
# 2
calculator("*", 3, 2)
# 6
calculator("/", 4, 2)
# 2
calculator("nope", 4, 2)
# "Invalid operation!"
# None