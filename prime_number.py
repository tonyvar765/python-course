def is_prime(x):
    if x<1:
        return False
    if x <3:
        return True
    if x%2==0 or x%3==0:
        return False

    i=5
    while i*i<=x:
        if x%i==0 or x%(i+2)==0:
            return False
        i+=6


    return True

number = int(input("enter the number"))
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")


