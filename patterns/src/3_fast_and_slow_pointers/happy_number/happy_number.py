# Time Complexity O(logN)
# The time complexity of the algorithm is difficult to determine. 
# However we know the fact that all unhappy numbers eventually get stuck in the cycle: 
# Example: 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4

# This sequence behavior tells us two things:
# If the number N is less than or equal to 1000, 
# then we reach the cycle or ‘1’ in at most 1001 steps.
# For N > 1000N, suppose the number has ‘M’ digits and the next number is ‘N1’. 

# (https://en.wikipedia.org/wiki/Happy_number)
# From the above Wikipedia link, we know that 
# the sum of the squares of the digits of ‘N’ is at most 9^2M, or 
# 81M (this will happen when all digits of ‘N’ are ‘9’).
# This means:
# N1 < 81M 
# As we know M = log(N+1)
# Therefore: N1 < 81 * log(N+1) => N1 = O(logN)
# This concludes that the above algorithm will have a time complexity of O(logN).

# Space Complexity O(1)
# The algorithm runs in constant space O(1).

def find_happy_number(num):
    slow, fast = num, num
    
    while True:
        slow = find_square_sum(slow)
        fast = find_square_sum(find_square_sum(fast))
        
        if slow == fast:
            break
    
    return slow == 1

def find_square_sum(num):
    _sum = 0
    
    while num > 0:
        digit = num % 10
        _sum += digit * digit
        num //= 10
    
    return _sum

print(find_happy_number(23))
print(find_happy_number(12))