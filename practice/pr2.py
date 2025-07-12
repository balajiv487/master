def generate_even_numbers_list(limit):
    n=[]
    for i in range(limit):
        if i %2==0:
            n.append(i)
    return n

print(generate_even_numbers_list(50))

def generate_even_numbers_generator(limit):
    for i in range(limit):
        if i % 2 == 0:
            yield i

print(list(generate_even_numbers_generator(10)))





