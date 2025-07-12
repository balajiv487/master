import re

def testPasswordStrength(password):
    eightCharsLongRegex=re.compile(r"[\w\d\s\W\D\S]{8,}")
    upperCaseRegex=re.compile(r"[A-Z]+")
    lowerCaseRegex=re.compile(r"[a-z]")
    oneOrMoreDigitRegex=re.compile(r"\d+")

    if not eightCharsLongRegex.search(password):
        return "Your password length should be at least 8 characters"
    elif not upperCaseRegex.search(password):
        return "Your password length should contain at least one uppercase character"
    elif not lowerCaseRegex.search(password):
        return "Your password length should contain at least one lowercase character"
    elif not oneOrMoreDigitRegex.search(password):
        return "Your password length should contain at least one digit b/w 0-9"
    return True
if __name__=="__main__":
    password=input("Enter your password: ")
print(testPasswordStrength(password))



