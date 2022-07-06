# Time O(2^N) 
# Space O(N)
# where N is the number of rings

NUM_PEGS = 3
def compute_towers_of_hanoi(num_of_rings):
    def compute_towers(num_of_rings, from_peg, to_peg, use_peg):
        if num_of_rings > 0:
            compute_towers(num_of_rings - 1, from_peg, use_peg, to_peg)
            pegs[to_peg].append(pegs[from_peg].pop())
            result.append([from_peg, to_peg])

            compute_towers(num_of_rings - 1, use_peg, to_peg, from_peg)

    result = []
    pegs = [list(reversed(range(1, num_of_rings + 1)))] + [[] for _ in range(1, NUM_PEGS)]

    compute_towers(num_of_rings, 0, 1, 2)

    return result

print(compute_towers_of_hanoi(3))

