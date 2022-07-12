# Basecase 
# When the input is equal to zero, we can return our result

# Work
# During every step: 
# We have to find the remainder of the current value when divided by 2
# And concatenate that remainder to the result
# Then we half the currrent value and  call the function with the new value

# Example Illustration
# | 0,    "111011"     -> answer
# | 1,    "11011"
# | 3,    "1011"
# | 7,    "011"
# | 14,   "11"
# | 29,   "1"
# | 59,   ""


def dec_to_binary(decimal):
    return solve_dec_to_binary(decimal, "")

def solve_dec_to_binary(decimal, result):
    if decimal == 0:
        return result
    
    result = str(decimal % 2) + result
    return solve_dec_to_binary(decimal // 2, result)

print(dec_to_binary(59))