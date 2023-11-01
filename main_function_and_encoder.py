# Program defines a function that displays the menu.
def menu():
    print("Menu")
    print("-" * 13)
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


# Program defines a function that takes in a user's inputted password and returns an encoded password with each digit
# being shifted up by 3 numbers.
def encode(password):
    new_password = ""
    for digit in password:
        if digit.isdigit():
            new_password += str((int(digit) + 3) % 10)
    return new_password


# Program runs the main function.
if __name__ == "__main__":
    while True:
        # Program displays the menu and asks for user's input.
        menu()
        user_input = input("Please enter an option: ")
        # If user inputs option 1, program asks for user's password and encodes it.
        if user_input == "1":
            user_password = input("Please enter your password to encode: ")
            encoded_password = encode(user_password)
            print("Your password has been encoded and stored!")
        # If user inputs option 3, program is ended.
        if user_input == "3":
            break
