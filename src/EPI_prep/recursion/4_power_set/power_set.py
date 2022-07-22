# Recursive Solution 
# Time O(n * 2^n)
# Space O(n)
def generate_power_set(input_set):

    def directed_power_set(to_be_selected, selected_so_far):
        if to_be_selected == len(input_set):
            power_set.append(list(selected_so_far))
            return
        
        directed_power_set(to_be_selected + 1, selected_so_far)
        directed_power_set(to_be_selected + 1, selected_so_far + [input_set[to_be_selected]])

    power_set = []
    directed_power_set(0, [])

    return power_set

print("Recursive Solution")
print(generate_power_set([0, 1, 2]))



# Iterative Solution
def generate_power_set_iter(A):
    subsets = []
    subsets.append([])

    for i in range(len(A)):
        curr_val = A[i]
        for j in range(len(subsets)):
            copy = subsets[j].copy()
            copy.append(curr_val)
            subsets.append(copy)
        
    return subsets

print("\nIterative Solution")
print(generate_power_set_iter([0, 1, 2]))