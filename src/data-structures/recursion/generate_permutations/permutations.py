# Time O(n * n!)
# since we do O(n) computation per call outside of the recursive calls.

# Space O(n!)
# Since the result set increases by the factorial of the length of array
# for eg:
# if array length = 1, length of result is = 1! which is = 1
# if array length = 2, length of result is = 2! which is = 2
# if array length = 3, length of result is = 3! which is = 6
# if array length = 4, length of result is = 4! which is = 24

# if the resulting array is ignored Space Complexity will be O(n), 
# Space O(n)
# Where N is the length of Array Aand the space represents the call stack
def permutations(A):
    def directed_permutation(i):
        if i == len(A) - 1:
            result.append(A.copy())
            return

        for j in range(i, len(A)):
            A[i], A[j] = A[j],  A[i]
            #Generate all permutations for A[i+1 :]
            directed_permutation(i+1)
            A[i], A[j] = A[j],  A[i]

    result = []
    directed_permutation(0)

    return result


print(len(permutations([7, 3, 5, 9, 10])))