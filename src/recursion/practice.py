def recursiveMethod(n):
    if n < 1:
        print("N is less than 1")
    else:
        recursiveMethod(n-1)
        print(n)
