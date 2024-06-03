import random

def otp_encrypt(message):
    key = [random.randint(0, 255) for _ in range(len(message))]
    encrypted_message = [(ord(char) + k) % 256 for char, k in zip(message, key)]
    return encrypted_message, key

def otp_decrypt(encrypted_message, key):
    decrypted_message = ''.join(chr((char - k) % 256) for char, k in zip(encrypted_message, key))
    return decrypted_message

def main():
    RED = "\033[91m"
    RESET = "\033[0m"
    BANNER = f"{RED}Made by protocolhere{RESET}"

    while True:
        print(BANNER)
        print("1. Encrypt")
        print("2. Decrypt")
        choice = input("Choose an option (1 or 2): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            encrypted_message, key = otp_encrypt(message)
            print(f"Encrypted Message (ASCII Values): {encrypted_message}")
            print(f"Key (ASCII Values): {key}")

        elif choice == '2':
            encrypted_message = input("Enter the encrypted message (comma-separated ASCII values): ")
            encrypted_message = [int(num) for num in encrypted_message.split(',')]
            key = input("Enter the key (comma-separated ASCII values): ")
            key = [int(num) for num in key.split(',')]
            decrypted_message = otp_decrypt(encrypted_message, key)
            print(f"Decrypted Message: {decrypted_message}")

        else:
            print("Invalid choice. Please enter 1 or 2.")
        
        # Option to exit or continue
        continue_choice = input("Do you want to perform another operation? (yes or no): ").strip().lower()
        if continue_choice != 'yes':
            break

if __name__ == "__main__":
    main()
