text=str("!$&',-.:;?QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm")
chars=sorted(list(set(text)))
vocal_size=len(chars)
print(chars)
print(vocal_size)
print(''.join(chars))
stoi={ch:i for i,ch in enumerate(chars)}
print(stoi)
itos={i:ch for i,ch in enumerate(chars)}
print(itos)
encode=lambda s: [stoi[i] for i in s]
decode=lambda l:"".join([itos[i]] for i in l)

print(encode("hi"))