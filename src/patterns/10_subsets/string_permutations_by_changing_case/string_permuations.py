from collections import deque

# Time complexity
# Since we can have 2^N2 permutations at the most and while processing each 
# permutation we convert it into a character array, the overall time complexity 
# of the algorithm will be O(N*2^N).

# Space complexity
# All the additional space used by our algorithm is for the output list. 
# Since we can have a total of O(2^N) permutations, 
# the space complexity of our algorithm is O(N*2^N).

def find_letter_case_string_permutations(str):
    permutations = []
    permutations.append(str)
    # process every character of the string one by one
    for i in range(len(str)):
        if str[i].isalpha():  # only process characters, skip digits
        # we will take all existing permutations and change the letter case appropriately
            n = len(permutations)
            for j in range(n):
                chars = list(permutations[j])
                # if the current character is in upper case, change it to lower case or vice versa
                chars[i] = chars[i].swapcase()
                permutations.append("".join(chars))
                 
    return permutations



print("String permutations are: " +
    str(find_letter_case_string_permutations("ad52")))
print("String permutations are: " +
    str(find_letter_case_string_permutations("ab7c")))
