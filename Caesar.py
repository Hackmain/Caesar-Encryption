def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def main():
    print("Welcome to the Simple Encryption App!")
    text = input("Enter the text you want to encrypt: ")
    shift = int(input("Enter the shift value for Caesar Cipher encryption: "))
    encrypted_text = caesar_cipher_encrypt(text, shift)
    print("Encrypted text:", encrypted_text)
    print("follow me in instagram esefkh740_")

if __name__ == "__main__":
    main()
