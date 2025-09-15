def greet():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")
    
def add_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}.")
    
def main():
    print("Welcome to the Function with Inputs program!")
    while True:
        print("\nChoose an option:")
        print("1. Greet")
        print("2. Add Numbers")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            greet()
        elif choice == '2':
            add_numbers()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
def substract_numbers(num1, num2):
    result = num1 - num2
    print(f"The difference between {num1} and {num2} is {result}.")
    
substract_numbers(10, 5)
    
            
main()            