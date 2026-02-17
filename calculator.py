def add(a, b): 
    return a + b 
 
def subtract(a, b): 
    return a - b 
 
def multiply(a, b): 
    return a * b 
 
def divide(a, b): 
    if b == 0: 
        return "Error: Division by zero" 
    return a / b 
 
def main(): 
    print("Simple Calculator") 
    print("1. Add") 
    print("2. Subtract") 
    print("3. Multiply") 
    print("4. Divide") 
 
    choice = input("Select operation (1-4): ") 
    a = float(input("Enter first number: ")) 
    b = float(input("Enter second number: ")) 
 
    if choice == '1': 
        print(f"Result: {add(a, b)}") 
    elif choice == '2': 
        print(f"Result: {subtract(a, b)}") 
    elif choice == '3': 
        print(f"Result: {multiply(a, b)}") 
    elif choice == '4': 
        print(f"Result: {divide(a, b)}") 
 
if __name__ == "__main__": 
    main() 
 
def square_root(a): 
    if a < 0: 
        return "Error: Cannot calculate square root of negative number" 
    return a ** 0.5 
