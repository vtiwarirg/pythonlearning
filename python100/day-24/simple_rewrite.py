# Simple Re-write Example - Easy to modify

print("🔄 SIMPLE FILE RE-WRITE EXAMPLE")
print("=" * 40)

# First write
print("\n1️⃣ Writing initial content...")
with open('my_file.txt', 'w') as file:
    file.write('First version of content\n')
    file.write('This will be replaced')

# Show what we wrote
with open('my_file.txt', 'r') as file:
    content = file.read()
print(f"Initial content:\n{content}")

# Re-write (overwrite) completely
print("\n2️⃣ Re-writing the file...")
with open('my_file.txt', 'w') as file:
    file.write('COMPLETELY NEW CONTENT!\n')
    file.write('The old content is gone\n')
    file.write('This is the new version')

# Show the new content
with open('my_file.txt', 'r') as file:
    new_content = file.read()
print(f"New content after re-write:\n{new_content}")

print("\n✅ Re-write successful! The file now contains completely different content.")