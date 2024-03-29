# Encoder that shifts all numbers up by 3
def password_encoder(password):
    # Ensure the input is exactly 8 digits long
    if len(password) != 8 or not password.isdigit():
        return "Error: Input must be an 8-digit string."

    # Shift each digit by 3 and handle wrapping from 9 to 0 using modulo
    encoded_string = "".join([str((int(char) + 3) % 10) for char in password])

    return encoded_string

# Decoder that shifts all numbers down by 3


def print_menu():
    while True:
        print("Menue")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        # Get user selection
        menu_option = int(input("\nPlease enter an option: "))

        if menu_option == 1:
            #
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!\n")
            encoded_password = password_encoder(password)

        elif menu_option == 2:


        elif menu_option == 3:
           break
# Print menu
def main():
    print_menu()


if __name__ == '__main__':
    main()