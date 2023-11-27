import string
import random
import secrets

def generate_random_password(length, character_list):
    generatepassword = [random.choice(character_list) for _ in range(length)]
    return ''.join(generatepassword)

def generate_secure_password(length):
    characters = string.ascii_letters + string.digits 
    generatepassword = ''.join(secrets.choice(characters) for _ in range(length))
    return generatepassword

def generate_strong_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation 
    generatepassword = ''.join(secrets.choice(characters) for _ in range(length))
    return generatepassword

def password_characters_length():
    while True:
        try:
            lengthofpassword = int(input("Enter the password length: "))
            if lengthofpassword >= 8:
                return lengthofpassword
            else:
                print("Atleast 8 characters required!")
        except ValueError:
            print("Invalid input")

if __name__ == "__main__":
    try:
        lengthofpassword = password_characters_length()

        while True:
            print('''Choose character set for password from these : 
                    1. Digits
                    2. Letters
                    3. Special characters
                    4. Exit''')

            character_list = ""

            # Getting character set for password
            while True:
                option = int(input("Select the option: "))
                if option == 1:
                    character_list += string.digits
                elif option == 2:
                    character_list += string.ascii_letters
                elif option == 3:
                    character_list += string.punctuation
                elif option == 4:
                    if not character_list:
                        print("Atleast 1 option must be selected before exiting")
                    else:
                        break
                else:
                    print("Select a valid option!")

            random_password = generate_random_password(lengthofpassword, character_list)
            print("Random Password:", random_password)

            secure_password = generate_secure_password(lengthofpassword)
            print("Secure Password:", secure_password)

            strong_password = generate_strong_password(lengthofpassword)
            print("Strong Password:", strong_password)

            generate_password_again = input("Do you want to generate password again? (yes/no): ").lower()
            if generate_password_again != "yes":
                break
    
    except ValueError:
        print("Invalid integer for password length")
