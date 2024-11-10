import random
import cmath
from math import sqrt, exp, log, log10, sin, cos, tan, radians, degrees, factorial, gcd, sinh, cosh, tanh
from statistics import mean, median, mode, stdev
import numpy as np

# Memory variable
memory = 0

# ============ Basic Arithmetic Operations ============
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def modulus(x, y):
    if y == 0:
        raise ValueError("Cannot perform modulus by zero!")
    return x % y

# ============ Advanced Math Operations ============
def sqroot(x):
    if x < 0:
        raise ValueError("Cannot take square root of a negative number!")
    return sqrt(x)

def exponential(x):
    return exp(x)

def log_base_10(x):
    if x <= 0:
        raise ValueError("Logarithm input must be positive!")
    return log10(x)

def natural_log(x):
    if x <= 0:
        raise ValueError("Logarithm input must be positive!")
    return log(x)

# ============ Trigonometric and Hyperbolic Functions ============
def sine(x):
    return sin(radians(x))

def cosine(x):
    return cos(radians(x))

def tangent(x):
    return tan(radians(x))

def hyperbolic_sine(x):
    return sinh(x)

def hyperbolic_cosine(x):
    return cosh(x)

def hyperbolic_tangent(x):
    return tanh(x)

# ============ Power and Root Functions ============
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def cube_root(x):
    return x ** (1/3)

def nth_root(x, n):
    return x ** (1/n)

# ============ Statistical Functions ============
def calculate_mean(data):
    return mean(data)

def calculate_median(data):
    return median(data)

def calculate_mode(data):
    return mode(data)

def calculate_std_dev(data):
    return stdev(data)

# ============ Combinatorial Functions ============
def calculate_combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def calculate_permutation(n, r):
    return factorial(n) // factorial(n - r)

# ============ Conversion Functions ============
def kilometers_to_miles(km):
    return km * 0.621371

def miles_to_kilometers(miles):
    return miles / 0.621371

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def decimal_to_binary(n):
    return bin(n)[2:]

# ============ Vector Operations ============
def vector_addition(A, B):
    return [a + b for a, b in zip(A, B)]

def vector_subtraction(A, B):
    return [a - b for a, b in zip(A, B)]

# ============ Matrix Operations ============
def matrix_addition(A, B):
    return np.add(A, B)

def matrix_multiplication(A, B):
    return np.dot(A, B)

# ============ Complex Number Operations ============
def complex_addition(a, b):
    return a + b

# ============ Memory Functions ============
def memory_store(value):
    global memory
    memory = value

def memory_recall():
    return memory

def memory_clear():
    global memory
    memory = 0

# Submenu for Basic Arithmetic
def arithmetic_menu():
    print("\n")
    print("1. Addition\t2. Subtraction\t3. Multiplication\t4. Division\t5. Modulus\t6. Back to Main Menu\n")

# Submenu for Advanced Math
def advanced_math_menu():
    print("\n")
    print("1. Square Root\t2. Exponential (e^x)\t3. Logarithm (base 10)\t4. Natural Logarithm\t5. Back to Main Menu\n")

# Submenu for Trigonometric and Hyperbolic Functions
def trig_hyperbolic_menu():
    print("\n")
    print("1. Sine\t2. Cosine\t3. Tangent\t4. Hyperbolic Sine\t5. Hyperbolic Cosine\t6. Hyperbolic Tangent\t7. Back to Main Menu\n")

# Submenu for Power and Root Functions
def power_root_menu():
    print("\n")
    print("1. Square\t2. Cube\t3. Cube Root\t4. nth Root\t5. Back to Main Menu\n")

# Submenu for Statistical Functions
def statistical_menu():
    print("\n:")
    print("1. Mean\t2. Median\t3. Mode\t4. Standard Deviation\t5. Back to Main Menu\n")

# Submenu for Combinatorial Functions
def combinatorial_menu():
    print("\n")
    print("1. Combination (nCr)\t2. Permutation (nPr)\t3. Back to Main Menu\n")

# Submenu for Conversion Functions
def conversion_menu():
    print("\n")
    print("1. Kilometers to Miles\t2. Celsius to Fahrenheit\t3. Decimal to Binary4. Back to Main Menu\n")

# Submenu for Vector Operations
def vector_menu():
    print("\n")
    print("1. Vector Addition\t2. Vector Subtraction\t3. Back to Main Menu\n")

# Submenu for Matrix Operations
def matrix_menu():
    print("\n")
    print("1. Matrix Addition\t2. Matrix Multiplication\t3. Back to Main Menu\n")

# Submenu for Complex Number Operations
def complex_menu():
    print("\n")
    print("1. Complex Addition\t2. Back to Main Menu\n")

# Submenu for Memory Functions
def memory_menu():
    print("\n")
    print("1. Memory Store\t2. Memory Recall\t3. Memory Clear\t4. Back to Main Menu\n")

# ============ Group Menus ============
def main_menu():
    print("\nCalculator Main Menu:")
    print("1. Basic Arithmetic Operations")
    arithmetic_menu()
    print("2. Advanced Math Operations")
    advanced_math_menu()
    print("3. Trigonometric and Hyperbolic Functions")
    trig_hyperbolic_menu()
    print("4. Power and Root Functions")
    power_root_menu()
    print("5. Statistical Functions")
    statistical_menu()
    print("6. Combinatorial Functions")
    combinatorial_menu()
    print("7. Conversion Functions")
    conversion_menu()
    print("8. Vector Operations")
    vector_menu()
    print("9. Matrix Operations")
    matrix_menu()
    print("10. Complex Number Operations")
    complex_menu()
    print("11. Memory Functions")
    memory_menu()
    print("12. Exit")



# ============ Main Calculator Loop ============
while True:
    main_menu()
    main_choice = int(input("Choose a category: "))

    # Basic Arithmetic
    if main_choice == 1:
        arithmetic_menu()
        arith_choice = int(input("Enter choice: "))
        if arith_choice == 1:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print("Result:", add(x, y))
        elif arith_choice == 2:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print("Result:", sub(x, y))
        elif arith_choice == 3:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print("Result:", mul(x, y))
        elif arith_choice == 4:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print("Result:", divide(x, y))
        elif arith_choice == 5:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print("Result:", modulus(x, y))
        elif arith_choice == 6:
            continue

    # Advanced Math Operations
    elif main_choice == 2:
        advanced_math_menu()
        adv_choice = int(input("Enter choice: "))
        if adv_choice == 1:
            x = float(input("Enter number: "))
            print("Result:", sqroot(x))
        elif adv_choice == 2:
            x = float(input("Enter number: "))
            print("Result:", exponential(x))
        elif adv_choice == 3:
            x = float(input("Enter number: "))
            print("Result:", log_base_10(x))
        elif adv_choice == 4:
            x = float(input("Enter number: "))
            print("Result:", natural_log(x))
        elif adv_choice == 5:
            continue

    # Trigonometric and Hyperbolic Functions
    elif main_choice == 3:
        trig_hyperbolic_menu()
        trig_choice = int(input("Enter choice: "))
        if trig_choice == 1:
            x = float(input("Enter angle in degrees: "))
            print("Result:", sine(x))
        elif trig_choice == 2:
            x = float(input("Enter angle in degrees: "))
            print("Result:", cosine(x))
        elif trig_choice == 3:
            x = float(input("Enter angle in degrees: "))
            print("Result:", tangent(x))
        elif trig_choice == 4:
            x = float(input("Enter angle: "))
            print("Result:", hyperbolic_sine(x))
        elif trig_choice == 5:
            x = float(input("Enter angle: "))
            print("Result:", hyperbolic_cosine(x))
        elif trig_choice == 6:
            x = float(input("Enter angle: "))
            print("Result:", hyperbolic_tangent(x))
        elif trig_choice == 7:
            continue

    # Power and Root Functions
    elif main_choice == 4:
        power_root_menu()
        pow_choice = int(input("Enter choice: "))
        if pow_choice == 1:
            x = float(input("Enter number: "))
            print("Result:", square(x))
        elif pow_choice == 2:
            x = float(input("Enter number: "))
            print("Result:", cube(x))
        elif pow_choice == 3:
            x = float(input("Enter number: "))
            print("Result:", cube_root(x))
        elif pow_choice == 4:
            x = float(input("Enter number: "))
            n = float(input("Enter root n: "))
            print("Result:", nth_root(x, n))
        elif pow_choice == 5:
            continue

    # Statistical Functions
    elif main_choice == 5:
        statistical_menu()
        stat_choice = int(input("Enter choice: "))
        if stat_choice == 1:
            data = list(map(float, input("Enter numbers separated by space: ").split()))
            print("Result:", calculate_mean(data))
        elif stat_choice == 2:
            data = list(map(float, input("Enter numbers separated by space: ").split()))
            print("Result:", calculate_median(data))
        elif stat_choice == 3:
            data = list(map(float, input("Enter numbers separated by space: ").split()))
            print("Result:", calculate_mode(data))
        elif stat_choice == 4:
            data = list(map(float, input("Enter numbers separated by space: ").split()))
            print("Result:", calculate_std_dev(data))
        elif stat_choice == 5:
            continue

    # Combinatorial Functions
    elif main_choice == 6:
        combinatorial_menu()
        comb_choice = int(input("Enter choice: "))
        if comb_choice == 1:
            n = int(input("Enter n: "))
            r = int(input("Enter r: "))
            print("Result:", calculate_combination(n, r))
        elif comb_choice == 2:
            n = int(input("Enter n: "))
            r = int(input("Enter r: "))
            print("Result:", calculate_permutation(n, r))
        elif comb_choice == 3:
            continue

    # Conversion Functions
    elif main_choice == 7:
        conversion_menu()
        conv_choice = int(input("Enter choice: "))
        if conv_choice == 1:
            km = float(input("Enter kilometers: "))
            print("Result:", kilometers_to_miles(km))
        elif conv_choice == 2:
            c = float(input("Enter Celsius: "))
            print("Result:", celsius_to_fahrenheit(c))
        elif conv_choice == 3:
            n = int(input("Enter decimal number: "))
            print("Result:", decimal_to_binary(n))
        elif conv_choice == 4:
            continue

    # Vector Operations
    elif main_choice == 8:
        vector_menu()
        vector_choice = int(input("Enter choice: "))
        if vector_choice == 1:
            A = list(map(int, input("Enter vector A elements separated by space: ").split()))
            B = list(map(int, input("Enter vector B elements separated by space: ").split()))
            print("Result:", vector_addition(A, B))
        elif vector_choice == 2:
            A = list(map(int, input("Enter vector A elements separated by space: ").split()))
            B = list(map(int, input("Enter vector B elements separated by space: ").split()))
            print("Result:", vector_subtraction(A, B))
        elif vector_choice == 3:
            continue

    # Matrix Operations
    elif main_choice == 9:
        matrix_menu()
        matrix_choice = int(input("Enter choice: "))
        if matrix_choice == 1:
            A = np.array(eval(input("Enter matrix A: ")))
            B = np.array(eval(input("Enter matrix B: ")))
            print("Result:", matrix_addition(A, B))
        elif matrix_choice == 2:
            A = np.array(eval(input("Enter matrix A: ")))
            B = np.array(eval(input("Enter matrix B: ")))
            print("Result:", matrix_multiplication(A, B))
        elif matrix_choice == 3:
            continue

    # Complex Number Operations
    elif main_choice == 10:
        complex_menu()
        complex_choice = int(input("Enter choice: "))
        if complex_choice == 1:
            a = complex(input("Enter complex number a (e.g., 1+2j): "))
            b = complex(input("Enter complex number b (e.g., 1+2j): "))
            print("Result:", complex_addition(a, b))
        elif complex_choice == 2:
            continue

    # Memory Functions
    elif main_choice == 11:
        memory_menu()
        memory_choice = int(input("Enter choice: "))
        if memory_choice == 1:
            value = float(input("Enter value to store: "))
            memory_store(value)
            print(f"Value {value} stored in memory.")
        elif memory_choice == 2:
            print(f"Memory Recall: {memory_recall()}")
        elif memory_choice == 3:
            memory_clear()
            print("Memory cleared.")
        elif memory_choice == 4:
            continue

    # Exit
    elif main_choice == 12:
        print("Exiting the calculator. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid category.")
