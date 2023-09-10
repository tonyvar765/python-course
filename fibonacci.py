def fibonacci(n):
    a,b=0,1
    fibonacci_series=[]
    if n<1:
        print('please enter a positive number')
    elif n==1:
        fibonacci_series.append(a)

    else:
        fibonacci_series=([a,b])

        for x in range(2,n):
            next_term=a+b
            fibonacci_series.append(next_term)
            a,b=b,next_term
        return fibonacci_series

n=int(input('enter the number: '))
result = fibonacci(n)
print(f"the fibonacci series are {result}")

