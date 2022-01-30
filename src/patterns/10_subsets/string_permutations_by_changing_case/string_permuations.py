from collections import deque

def find_letter_case_string_permutations(str):
    permutations = []
    alphabets_in_word = []
    for char in str:
        if char.isalpha():
            alphabets_in_word.append(char)
    
    subsets = []  
    subsets.append([])
    for char in alphabets_in_word:
        n = len(subsets)
        
        for i in range(n):
            curr_subset = list(subsets[i])
            curr_subset.append(char)
            subsets.append(curr_subset)
    
    for subset in subsets:
        if len(subset) == 0:
            permutations.append(str)
        else:
            new_permutation = str
            for char in subset:
                index = new_permutation.find(char)
                new_str = list(new_permutation)
                new_str[index] = char.upper()
                new_permutation = "".join(new_str)
                                          
            permutations.append(new_permutation)
        
    return permutations



print("String permutations are: " +
    str(find_letter_case_string_permutations("ad52")))
print("String permutations are: " +
    str(find_letter_case_string_permutations("ab7c")))
