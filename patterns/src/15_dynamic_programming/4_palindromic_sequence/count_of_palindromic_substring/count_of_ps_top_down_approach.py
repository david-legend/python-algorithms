def count_PS(str):
    n = len(str)
    return count_PS_recursive(str, 0, n-1)

def count_PS_recursive(str, start_idx, end_idx):
    pass



def main():
    print("Recursive Solution Without Memoization")
    print(count_PS("abdbca"))
    print(count_PS("cddpd"))
    print(count_PS("pqr"))
    
    # print("\n\nRecursive Solution With Memoization")
    # print(count_PS_dp("abdbca"))
    # print(count_PS_dp("cddpd"))
    # print(count_PS_dp("pqr"))
    
main()