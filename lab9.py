# Takes a string of numbers, and returns a string of the numbers after adding 3. 
# You will implement this function in your repository.
# Examples:
# “12345555” will become “45678888” after encoding.
# “00009962” will become “33332295” after encoding.

def encode(password):
    encode_pass = ""
    for num in password:
        encode_pass = encode_pass + str(int(num) + 3)

    return encode_pass


# Takes a string of numbers, and returns a string of the numbers after subtracting 3.
# You will implement this function in your partner’s repository.
def decode(password):
    decoded_chars = []
    for char in password:
        decoded_char = str((int(char) + 3) % 10)
        decoded_chars.append(decoded_char)
    return ''.join(decoded_chars)


def printMenu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")


def main():
    printMenu()

    while True:

        option = input("Please enter an option: ")

        if option == '1':
            password = input("Please enter the password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif option == '2':

            try:
                decoded_password = decode(password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            except:
                print("Why haven't you put in a password?")
        elif option == '3':
            break


if __name__ == "__main__":
    main()
