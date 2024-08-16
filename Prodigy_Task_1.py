def caesar_cipher(text, shift, decrypt=False):
    result = []
    if decrypt:
        shift = -shift
    
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result.append(shifted_char)
        else:
            result.append(char)
    
    return ''.join(result)

def main():
    while True:
        mode = input("Choose an option - Encrypt (e), Decrypt (d), Close (c): ").strip().lower()
        if mode in ['e', 'd', 'c']:
            if mode == 'c':
                print("Closing the program. Goodbye!")
                return        
            break    
        print("Invalid option. Please choose 'e' for Encrypt, 'd' for Decrypt, or 'c' to Close the program.")
        

    text = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift value: "))
    except ValueError:
        print("Shift value must be an integer.")
        return

    decrypt = mode == 'd'
    processed_text = caesar_cipher(text, shift, decrypt)
    action = "Decrypted" if decrypt else "Encrypted"
    print(f"{action} message: {processed_text}")

if __name__ == "__main__":
    main()
