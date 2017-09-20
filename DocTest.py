def factorial(x):
    x=int(x)
    k=x
    total=1
    while x<=k and x > 0:
        total=total*x
        x=x-1
    print(total)