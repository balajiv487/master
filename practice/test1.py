n=int(input("Enter a number to check prime or not:"))
for i in range(2,n):
    print(i)
    if n%i==0:
        print("Given number is not prime")
        break
else:
    print("Give number is a prime number")