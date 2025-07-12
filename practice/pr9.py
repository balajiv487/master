from enum import Enum
class Color(Enum):
    red=1
    green=2
    blue=3
print(Color.red.name)
print(Color.red.value)
for i in Color:
    print(i)