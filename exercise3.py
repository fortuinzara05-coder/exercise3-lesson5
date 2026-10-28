# Question 1: Basic Function Definition and Calling

#TODO: define a function called "greet" that prints "Hello, World!"
def greet():
    print("Hello, World!")

# Call the function
greet()

#------------------------------------------------------------------------------------
# Question 2: Function with Parameters
#TODO: define a function called "personalized_greeting" that takes a name as a parameter and prints a personalized greeting
def personalized_greeting(name):
    print(f"Hello, {name}!")

# Call the function with a name
personalized_greeting("Yaya")

#------------------------------------------------------------------------------------
# Question 3: Function with Return Value
#TODO: define a function called "square" that takes a number as a parameter and returns its square
def square(number):
    return number ** 2

# Call the function and print the result
result = square(5)
print(f"The square of 5 is: {result}")

#------------------------------------------------------------------------------------
# Question 4: Function with Multiple Parameters and Return Value
#TODO: define a function called "rectangle_area" that takes length, width as parameters and returns the area of the rectangle
def rectangle_area(length, width):
    return length * width

# Call the 'rectangle_area' function with length 4 and width 5, and print the result
area = rectangle_area(4, 5)
print(f"The area of the rectangle is: {area}")

#------------------------------------------------------------------------------------
# Question 5: Using a Function as an Argument
#TODO: define a function called "apply_operation" that takes a function and a number as parameters, and returns the result of applying the function to the number
def apply_operation(func, number):
    return func(number)


# TODO: define a function called "double" that takes a number as a parameter and returns its double
def double(number):
    return number * 2

# Call the 'apply_operation' function with the 'double' function and the number 7, and print the result
result = apply_operation(double, 7)
print(f"The double of 7 is: {result}")

# call the 'apply_operation' function with the 'square' function (defined in Question 3) and the number 3, and print the result
result = apply_operation(square, 3)
print(f"The square of 3 is: {result}")

