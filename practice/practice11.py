def is_prime(n):
    print (f"Number is : {n} ")
    if n==0:
        return "0 is not prime"
    elif n==1:
        return "1 is not prime"
    else:
        for i in range(2,n):
            if n%i==0:
                return "Given number is not a prime"
            break
        return "Given number is prime"

print(is_prime(10))


def max_list(l):
    print(f"inout list is: {l}")
    e=max(l)
    return e

l=[4,6,9,0,8]
print(max_list(l))


