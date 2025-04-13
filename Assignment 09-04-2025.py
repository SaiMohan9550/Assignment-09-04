#Assignment on Class

# 1. Define a class Person with attributes name and age. Create an object of this class and print its attributes.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person1 = Person("Sai Mohan", 21)
print("Name:", person1.name)
print("Age:", person1.age)


# 2. Create a class Rectangle with attributes length and width. Include a method to calculate the area of the rectangle.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
rect = Rectangle(7, 3)
print("Area of rectangle:", rect.area())


# 3. Implement a BankAccount class with methods to deposit and withdraw money. Ensure that the balance does not go negative.

class BankAccount:
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}, New Balance: {self.balance}")
account = BankAccount()
account.deposit(30000)
account.withdraw(10000)
account.withdraw(15000)


# 4. Design a class Student with attributes name and marks. Include a method that calculates the grade based on marks.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 40:
            return "D"
        else:
            return "F"
student1 = Student("Mohan Sai", 88)
print(f"Student Name: {student1.name}")
print(f"Marks: {student1.marks}")
print(f"Grade: {student1.grade()}")


# 5. Write a Vehicle class with a method description() that prints the vehicle type. Create a subclass Car that inherits from Vehicle and overrides the description() method.

class Vehicle:
    def description(self):
        print("This is a vehicle.")
class Car(Vehicle):
    def description(self):
        print("This is a car.")
v = Vehicle()
v.description()
c = Car()
c.description()



# Assignment on Functions

# 1. Write a function add_numbers(a, b) that returns the sum of two numbers.

def add_numbers(a, b):
    return a + b
print("Sum:", add_numbers(14, 17))


# 2. Create a function factorial(n) that calculates the factorial of a given number using recursion.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of 7:", factorial(7))


# 3. Implement a function is_prime(n) that checks if a number is prime.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print("Is 5 prime?", is_prime(5))
print("Is 9 prime?", is_prime(9))


# 4. Define a function reverse_string(s) that returns the reverse of a given string.

def reverse_string(s):
    return s[::-1]
print("Reversed string:", reverse_string("THIS IS PYTHON"))


# 5. Write a function fibonacci(n) that returns the first n numbers in the Fibonacci sequence.

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
print("Fibonacci sequence (first 9 numbers):", fibonacci(9))
