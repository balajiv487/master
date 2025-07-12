def pass_by_value(name):
    name=f"Hello {name}"
    print(name)
name="Balaji"
pass_by_value(name)
print(name)

def pass_by_reference(data):
    data.extend(data)
    print(data)

b = ["Professor", "Lisbon", "Nairobi", "Tokyo", "Berlin"]
pass_by_reference(b)
print(b, end=" \n")