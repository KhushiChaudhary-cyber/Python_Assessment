# Program: Caesar Cipher Encryption and Decryption
# This program encrypts and decrypts a message
# using Caesar Cipher technique

# Function to encrypt message
def encrypt_message(message, shift):
    encrypted_text = ""

    for ch in message:
        if ch.isalpha():
            # Handle uppercase letters
            if ch.isupper():
                encrypted_text += chr((ord(ch) - 65 + shift) % 26 + 65)

            # Handle lowercase letters
            else:
                encrypted_text += chr((ord(ch) - 97 + shift) % 26 + 97)

        else:
            encrypted_text += ch

    return encrypted_text


# Function to decrypt message
def decrypt_message(message, shift):
    decrypted_text = ""

    for ch in message:
        if ch.isalpha():
            # Handle uppercase letters
            if ch.isupper():
                decrypted_text += chr((ord(ch) - 65 - shift) % 26 + 65)

            # Handle lowercase letters
            else:
                decrypted_text += chr((ord(ch) - 97 - shift) % 26 + 97)

        else:
            decrypted_text += ch

    return decrypted_text


# Take input from user
original_message = input("Enter message: ")
shift_value = int(input("Enter shift value: "))

# Encrypt message
encrypted_message = encrypt_message(original_message, shift_value)

# Decrypt message
decrypted_message = decrypt_message(encrypted_message, shift_value)

# Display results
print("\nEncrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)

'''output:
Enter message: Hello World
Enter shift value: 3
Encrypted Message: Khoor Zruog
Decrypted Message: Hello World
'''