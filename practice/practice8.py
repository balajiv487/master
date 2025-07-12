import random
import string

ch=string.ascii_letters+string.digits+string.punctuation
password="".join(random.choice(ch) for _ in range(15))
print("Generate Passord:",password)