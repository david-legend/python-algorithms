import bintrees

def close_entries(input):
    tree = bintrees.RBTree()
    curr_interval = [None] * len(input)

    for idx, sorted_array in enumerate(input):
        it = iter(sorted_array)
        first_min_val = next(it, None)

        if first_min_val is not None:
            curr_interval[idx] = first_min_val
            tree.insert((first_min_val, idx), it)
    
    min_so_far = float('inf')
    result = []
    while True:
        min_val, idx = tree.min_key()
        max_val = tree.max_key()[0]
        current_min = max_val - min_val
        if current_min < min_so_far:
            min_so_far = current_min
            result = list(curr_interval)
            

        it = tree.pop_min()[1]
        next_min_val = next(it, None)

        if next_min_val is None:
            return result
        
        curr_interval[idx] = next_min_val
        tree.insert((next_min_val, idx), it)




print(close_entries([[1,10,15],[1,6,9,12,15],[1,16,24]]))
print(close_entries([[5,10,15],[3,6,9,12,15],[8,16,24]]))