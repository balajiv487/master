def encrypt(text,key=0):
    if not isinstance(text,str):
        raise TypeError("{} should be a string".format(text))
    if not isinstance(key,int):
        raise TypeError("{} should be an integer".format(key))
    return "".join([chr(ord(i)+key) for i in text ])

def decrypt(text, key=0):
    if not isinstance(text, str):
        raise TypeError("{} should be a type string".format(text))
    if not isinstance(key, int):
        raise TypeError("{} should be of type int".format(key))
    return "".join([chr(ord(something) - key) for something in text])

