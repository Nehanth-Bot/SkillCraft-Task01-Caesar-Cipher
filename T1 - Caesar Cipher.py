def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr(
                (ord(char) - ord('A') + shift) % 26
                + ord('A')
            )

        elif char.islower():
            result += chr(
                (ord(char) - ord('a') + shift) % 26
                + ord('a')
            )

        else:
            result += char

    return result


def decrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr(
                (ord(char) - ord('A') - shift) % 26
                + ord('A')
            )

        elif char.islower():
            result += chr(
                (ord(char) - ord('a') - shift) % 26
                + ord('a')
            )

        else:
            result += char

    return result


def save_to_file(content):
    try:
        with open("output.txt", "a") as file:
            file.write(content + "\n")

        print("\nResult saved to output.txt")

    except Exception as e:
        print(f"\nError saving file: {e}")


def get_shift():
    while True:
        try:
            shift = int(input("Enter shift value: "))
            return shift

        except ValueError:
            print("Please enter a valid number.")


def main():

    print("\n===== Caesar Cipher Program =====")

    while True:

        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            message = input("Enter message: ")
            shift = get_shift()

            encrypted = encrypt(message, shift)

            print("\nEncrypted Message:")
            print(encrypted)

            save_to_file(
                f"Encrypted | Original: {message} | Shift: {shift} | Result: {encrypted}"
            )

        elif choice == "2":

            message = input("Enter encrypted message: ")
            shift = get_shift()

            decrypted = decrypt(message, shift)

            print("\nDecrypted Message:")
            print(decrypted)

            save_to_file(
                f"Decrypted | Input: {message} | Shift: {shift} | Result: {decrypted}"
            )

        elif choice == "3":

            print("\nThank you for using Caesar Cipher!")
            break

        else:

            print("\nInvalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()