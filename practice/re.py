import re

match_object=re.search("Hello","Hello World")
print(match_object)

match_object1 = re.search(r'world', 'hello world hello world')
print(match_object1)

match_object3 = re.search(r'world', 'hello universe')
print(match_object3)

match_object = re.match(r'hello', 'hello world')

print(match_object)

match_object1 = re.match(r'world', 'hello world')

print(match_object1)



match_object = re.fullmatch(r'hello', 'hello')

print(match_object)

match_object1 = re.fullmatch(r'hello', 'hello hello world')

print(match_object1)

matches=re.findall("hello","hello hello world")
print(matches)

new_string = re.sub(r'hello', 'hi', 'hello world hello')

print(new_string)

pattern = re.compile(r'hello')

match_object = pattern.search('hello world')

print(match_object.group())