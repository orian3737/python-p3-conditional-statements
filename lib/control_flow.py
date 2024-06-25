#!/usr/bin/env python3

def admin_login(username, password):
    if (username == "admin" or username == "ADMIN") and password == "12345":
        result = "Access granted"
    else:
        result = "Access denied"
    print(result)
    return result

def hows_the_weather(temperature):
    if temperature < 40:
        result = "Brisk!"
    elif 40 <= temperature <= 65:
        result = "It's a little chilly out there!"
    elif temperature > 85:
        result = "It's too dang hot out there!"
    else:
        result = "Perfect!"
    print(result)
    return result

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        result = "FizzBuzz"
    elif num % 3 == 0:
        result = "Fizz"
    elif num % 5 == 0:
        result = "Buzz"
    else:
        result = num
    print(result)
    return result

def calculator(operation, num1, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        result = "Invalid operation!"
    print(f"Result of {num1} {operation} {num2}: {result}")
    return result

# Testing the functions
admin_login("sudo", "12345")
admin_login("admin", "12345")
admin_login("ADMIN", "12345")

hows_the_weather(33)
hows_the_weather(99)
hows_the_weather(75)
hows_the_weather(60)

fizzbuzz(1)
fizzbuzz(2)
fizzbuzz(3)
fizzbuzz(4)
fizzbuzz(5)
fizzbuzz(15)

calculator("+", 1, 1)
calculator("-", 3, 1)
calculator("*", 3, 2)
calculator("/", 4, 2)
calculator("nope", 4, 2)
