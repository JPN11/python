# Python program that solves trigonometry
import sys
import math

def calculate_trig_function(func_name, angle):
    """Calculate the trigonometric function based on the function name."""
    trig_functions = {
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan
    }
    
    if func_name in trig_functions:
        return trig_functions[func_name](math.radians(angle))
    else:
        return None

def main():
    # Check if the user provided the required command line arguments
    if len(sys.argv) != 2:
        print("Usage: python trig.py <trig function>")
        return

    func_name = sys.argv[1]
    angle = float(input("Enter the angle in degrees: "))
    
    result = calculate_trig_function(func_name, angle)
    
    if result is not None:
        print(f"The {func_name} of the angle is: {result}")
    else:
        print("Invalid trigonometric function. Please use 'sin', 'cos', or 'tan'.")

if __name__ == "__main__":
    main()