# Base case
# the smallest input we can pass is an empty string or a single char
# In this case, both inputs passes as a palindrome

# Work
# The least amount of work we can do is to compare the characters 
# at the first and last position of the string. 
# If they are equal then we can call the function again
# But if they are not then we can return false

# Call stack illustration - input - "kayak"

# | "y"          --> return true
# | "aya"        --> return true
# | "kayak"      --> return true

# Call stack illustration - input - "racecar"

# | "e"            --> return true
# | "cec"          --> return true
# | "aceca"        --> return true
# | "racecar"      --> return true

def is_palindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True
    
    last_char_idx = len(s) - 1
    if s[0] == s[last_char_idx]:
        return is_palindrome(s[1 : last_char_idx])
    
    return False


print(is_palindrome("kayak")) # True
print(is_palindrome("racecar")) # True
print(is_palindrome("bollocks")) # False
print(is_palindrome("madam")) # True
