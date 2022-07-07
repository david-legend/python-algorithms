def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)
         
print(gcd(156, 36)) #4
print(gcd(64, 36)) #4