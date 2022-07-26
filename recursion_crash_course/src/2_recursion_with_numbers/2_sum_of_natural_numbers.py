def sum_natural_numbers(val):
    if val <= 1:
        return val
    
    return val + sum_natural_numbers(val - 1)


print(sum_natural_numbers(10)) # 55
print(sum_natural_numbers(7)) # 28