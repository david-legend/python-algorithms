def decToBinary(n):
    assert int(n) == n, "Number must be an integer"
    if n == 1:
        return 1
    else:
        if(n > 0):
            return str(decToBinary(int(n/2))) + str((n%2))
        else:
            return str('-') + str(decToBinary(abs(int(n/2)))) + str((n%2)) 

print(decToBinary(-89))


def decToBinary2(n):
    assert int(n) == n, "Number must be an integer"
    if n == 0:
        return 0
    else:
        (n%2) + 10 * decToBinary2(int(n/2))


print(decToBinary2(-89))