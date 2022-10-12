def letter_code_perm(input):
    def letter_code_perm_helper(data, idx, n):
        if idx >= n:
            result.append("".join(list(data)))
            return 
        
        if ord('0') <= ord(input[idx]) <= ord('9'):
            data.append(input[idx])
            letter_code_perm_helper(data, idx + 1, n)
            data.pop()
            return
        
        data.append(input[idx])
        letter_code_perm_helper(data, idx + 1, n)

        data.pop()

        data.append(input[idx].upper())
        letter_code_perm_helper(data, idx + 1, n)
        data.pop()

    result = []
    letter_code_perm_helper([], 0, len(input))
    return result


print(letter_code_perm("3yx8")) # [["a1"], ["A1"]]