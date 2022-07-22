# Time O(2^n)
# Space O(n) when n is the length of the string
def palindromic_decompostions(input):
    def directed_palindromic_decompostions(i):
        if i >= len(input):
            result.append(list(partition))

        for j in range(i, len(input)):
            if is_palindrome(input, i, j):
                partition.append(input[i:j+1])
                directed_palindromic_decompostions(j+1)
                partition.pop()
            
    result, partition = [], []
    directed_palindromic_decompostions(0)

    return result

def is_palindrome(input, left, right):
    while left < right:
        if input[left] != input[right]:
            return False
        left, right = left + 1, right - 1
    
    return True

print(palindromic_decompostions("1414")) # [['1', '4', '1', '4'], ['1', '414'], ['141', '4']]
print(palindromic_decompostions("1234")) #[['1', '2', '3', '4']]
print(palindromic_decompostions("0204451881")) # [['0', '2', '0', '4', '4', '5', '1', '8', '8', '1'], ['0', '2', '0', '4', '4', '5', '1', '88', '1'], ['0', '2', '0', '4', '4', '5', '1881'], ['0', '2', '0', '44', '5', '1', '8', '8', '1'], ['0', '2', '0', '44', '5', '1', '88', '1'], ['0', '2', '0', '44', '5', '1881'], ['020', '4', '4', '5', '1', '8', '8', '1'], ['020', '4', '4', '5', '1', '88', '1'], ['020', '4', '4', '5', '1881'], ['020', '44', '5', '1', '8', '8', '1'], ['020', '44', '5', '1', '88', '1'], ['020', '44', '5', '1881']]