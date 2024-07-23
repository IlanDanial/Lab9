# Takes a string of numbers, and returns a string of the numbers after adding 3. 
# You will implement this function in your repository.
# Examples:
# “12345555” will become “45678888” after encoding.
# “00009962” will become “33332295” after encoding.

def encode(password):
    encode_pass = ""
    for num in password:
        encode_pass = encode_pass + str(int(num)+3)
    
    return encode_pass

# Takes a string of numbers, and returns a string of the numbers after subtracting 3.
# You will implement this function in your partner’s repository.
def decode(password):
    pass

def printMenu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")

def main():
    pass

if __name__ == "__main__":
    main()