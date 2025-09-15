print("Welcome to the Caesar Cipher program!")
alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]

def caesar(original_text, shift_amount, encode_or_decode): 
    output_text = ""
    shift_amount = shift_amount % len(alphabet)  # Normalize shift

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter  # Keep non-alphabet characters unchanged
    print(f"The {encode_or_decode}d text is: {output_text}")        
    return output_text

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    
    restart = input("Do you want to restart the program? Type 'yes' or 'no': ").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")
    elif restart != "yes":
        print("Invalid input. Please type 'yes' or 'no'.")
    else:
        print("Restarting the program...")