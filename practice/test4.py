import reques

r = requests.get('https://api.genderize.io?name=luc', auth=('user', 'pass'))
print("Status Code:",r.status_code)
print("Server:",r.headers.get("Server"))
print("Date:",r.headers.get("Date"))
print(("Encoding:",r.encoding))
print("text:",r.text)
print("Json:",r.json())
print("connection:",r.connection)
print("content",r.content)
print("raw",r.raw)
print("history",r.history)