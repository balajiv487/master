import random
import string


def main():
    print("_____________________________________")
    print(" Welcome to this Password Generator ")
    print("-------------------------------------\n")
    try:
        length=int(input("Enter the length of the password: "))
    except:
        print("input numbers only")
    password_length=0
    while password_length<=length:
        print("Your password must have at least 8 characters")
        password_length=getPasswordLength()
    all_characters =get_characters()
    password =generatePassword(all_characters, password_length)
    print("\nYour password is: " + password)
    print("__________________________________________")
    print("| Thanks for using the Password Generator |")
    print("------------------------------------------")
def getPasswordLength():
    password_length=int(input("Enter the password length:"))
    return password_length

def get_characters():
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    num=string.digits
    symbol=string.punctuation
    all_characters=lower+upper+num+symbol
    return all_characters
def generatePassword(password_length,all_characters):
    password="".join(random.sample(all_characters,password_length))
    return password

main()