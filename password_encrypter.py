def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode(password):
    new_pass = ''
    for i in password:
        new_pass += str(int(i) + 3)
    print("Your password has been encoded and stored!")
    return new_pass

def main():
    menu()
    while True:
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encode(password)
        elif option == 2:
            pass
        else:
            break
