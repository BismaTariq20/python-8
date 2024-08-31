# 1. Calculate age based on current year and birth year
def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return f"My age is {age}"

print(calculate_age(2024, 2002))

# 2. Calculate area of a rectangle
def calculate_rectangle_area(length, width):
    area = length * width
    return f"The area of the rectangle is {area}"

print(calculate_rectangle_area(5, 3))

# 3. Calculate area of a circle
import math

def calculate_circle_area(radius):
    area = math.pi * (radius ** 2)
    return f"The area of the circle is {area}"

print(calculate_circle_area(4))

# 4. Calculate area of a cube
def calculate_cube_area(side_length):
    area = 6 * (side_length ** 2)
    return f"The surface area of the cube is {area}"

print(calculate_cube_area(4))

# 5. Convert temperature from Fahrenheit to Celsius and vice versa
def convert_temperature(temp, from_unit, to_unit):
    if from_unit == "F" and to_unit == "C":
        return (temp - 32) * 5 / 9
    elif from_unit == "C" and to_unit == "F":
        return (temp * 9 / 5) + 32
    else:
        return "Invalid units"

def print_temperature_conversion(temp, from_unit, to_unit):
    result = convert_temperature(temp, from_unit, to_unit)
    if result != "Invalid units":
        print(f"{temp}{from_unit} is equal to {result}{to_unit}")
    else:
        print(result)

print_temperature_conversion(100, "F", "C")
print_temperature_conversion(37.5, "C", "F")

# 6. Convert seconds to minutes and seconds
def convert_seconds_to_minutes(total_seconds):
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{total_seconds} seconds is equal to {minutes} minutes and {seconds} seconds"

print(convert_seconds_to_minutes(120))

# 7. Calculate percentage
def calculate_percentage(part, whole):
    return (part / whole) * 100

def print_percentage(part, whole):
    percentage = calculate_percentage(part, whole)
    print(f"{part} is {percentage}% of {whole}")

print_percentage(25, 100)

# 8. BMI Calculator
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return f"Weight: {weight} kg\nHeight: {height} m\nBMI: {round(bmi, 2)}"

print(calculate_bmi(58, 1.52))

# 9. Cylinder Volume Calculator

import math
def calculate_cylinder_volume(radius, height):
    volume = math.pi * (radius ** 2) * height
    return f"Radius: {radius}\nHeight: {height}\nVolume: {round(volume, 2)}"

print(calculate_cylinder_volume(5, 10))