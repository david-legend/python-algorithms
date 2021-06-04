def greatestCommonDivisor(a, b):
    assert int(a) == a and int(b) == b, "Values should be integers"
    if b == 0:
        return a
    else:
        return greatestCommonDivisor(abs(b), abs(a) % abs(b))


print(greatestCommonDivisor(48, -18))