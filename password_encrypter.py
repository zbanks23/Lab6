def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")

def encode(password):
    new_pass = ''
    for i in password:
        if i == "7":
            new_pass += "0"
        elif i == "8":
            new_pass += "1"
        elif i == "9":
            new_pass += "2"
        else:
            new_pass += str(int(i) + 3)
    return new_pass

def main():
    menu()
    while True:
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            pass
        else:
            break

if __name__ == "__main__":
    main()