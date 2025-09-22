# Simple File Writing Example

# Write to file
try:
    with open('snake.txt', 'w') as file:
        file.write('new testing')
    print("File written successfully!")
except Exception as e:
    print(f"Error: {e}")

# Read and display the content to verify
try:
    with open('snake.txt', 'r') as file:
        content = file.read()
        print(f"File content: {content}")
except Exception as e:
    print(f"Error reading file: {e}")