def powerOfNumber(base, power):
    assert int(power) == power, "Power must be positive integer"
    if power == 0:
        return 1

    if power == 1:
        return base

    if(power > 0):
        return base * powerOfNumber(base, power-1)
    else:
        return 1 / base * powerOfNumber(base, power+1)


print(powerOfNumber(2, 1))

# TODO Add case to compute decimal powers