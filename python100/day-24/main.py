# Demonstrating File Re-writing Operations

print("=" * 60)
print("FILE RE-WRITING DEMONSTRATION")
print("=" * 60)

def show_file_content(filename):
    """Helper function to display file content"""
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print(f"\n   📄 Current content of {filename}:")
        print("   " + "-" * 40)
        if content.strip():
            for i, line in enumerate(content.split('\n'), 1):
                if line:
                    print(f"   Line {i}: {line}")
        else:
            print("   (File is empty)")
        print("   " + "-" * 40)
        print(f"   File size: {len(content)} characters")
    except FileNotFoundError:
        print(f"   📄 {filename} does not exist yet")

# Step 1: Initial write
print("\n🔹 STEP 1: Initial write to file")
with open('snake.txt', 'w') as file:
    file.write('Original content\n')
    file.write('This is the first version\n')
    file.write('Line 3 of original')
print("   ✓ Initial content written")
show_file_content('snake.txt')

# Step 2: Re-write (overwrite) the entire file
print("\n🔹 STEP 2: Re-writing (overwriting) the file")
print("   (Using 'w' mode - this REPLACES all content)")
with open('snake.txt', 'w') as file:
    file.write('NEW CONTENT - All old content is gone!\n')
    file.write('This completely replaces the previous content\n')
    file.write('Hello, my name is Virendra Tiwari\n')
    file.write('Learning file re-writing in Python')
print("   ✓ File completely rewritten")
show_file_content('snake.txt')

# Step 3: Demonstrate append mode (NOT overwriting)
print("\n🔹 STEP 3: Appending to file (NOT overwriting)")
print("   (Using 'a' mode - this ADDS to existing content)")
with open('snake.txt', 'a') as file:
    file.write('\n--- APPENDED CONTENT ---\n')
    file.write('This is added to the end\n')
    file.write('Original content remains')
print("   ✓ Content appended")
show_file_content('snake.txt')

# Step 4: Another complete rewrite
print("\n🔹 STEP 4: Another complete re-write")
print("   (Again using 'w' mode - erases everything and starts fresh)")
with open('snake.txt', 'w') as file:
    file.write('FINAL VERSION\n')
    file.write('This is the final rewritten content\n')
    file.write('All previous content is gone again!')
print("   ✓ File rewritten again")
show_file_content('snake.txt')

print("\n" + "=" * 60)
print("KEY POINTS ABOUT RE-WRITING:")
print("• 'w' mode = OVERWRITES (replaces all content)")
print("• 'a' mode = APPENDS (adds to existing content)")
print("• 'w' mode creates file if it doesn't exist")
print("• 'w' mode truncates (empties) file if it exists")
print("=" * 60)