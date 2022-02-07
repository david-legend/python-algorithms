from collections import deque

# Time complexity 
# In step ‘d’, each task can become a source only once 
# and each edge (a rule) will be accessed and removed once. 
# Therefore, the time complexity of the above algorithm will be O(V+E), 
# where ‘V’ is the total number of different characters 
# and ‘E’ is the total number of the rules in the alien language. 
# Since, at most, each pair of words can give us one rule, 
# therefore, we can conclude that the upper bound for the rules is O(N), 
# where ‘N’ is the number of words in the input. 
# So, we can say that the time complexity of our algorithm is O(V+N).

# Space complexity 
# The space complexity will be O(V+N), 
# since we are storing all of the rules for each character in an adjacency list.

def find_order(words):
    if len(words) == 0:
        return ""
    
    # initialize graph
    in_degrees = {}
    graph = {}
    for word in words:
        for char in word:
            in_degrees[char] = 0
            graph[char] = []
    
    # build graph
    for i in range(len(words) - 1):
        word_1, word_2 = words[i], words[i+1]
        for j in range(min(len(word_1), len(word_2))):
            parent, child = word_1[j], word_2[j]
            if word_1[j] != word_2[j]:
                graph[parent].append(child)
                in_degrees[child] += 1
                break
                
    # find sources
    sources = deque()
    for vertex in in_degrees:
        if in_degrees[vertex] == 0:
            sources.append(vertex) 
             
    # reduce in degrees and update sources
    sorted_order = []
    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for adj_vertex in graph[vertex]:
            in_degrees[adj_vertex] -= 1
            if in_degrees[adj_vertex] == 0:
                sources.append(adj_vertex)
    
    if len(sorted_order) != len(in_degrees):
        return ""
    
    return ''.join(sorted_order)


def main():
    print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
    print("Character order: " + find_order(["cab", "aaa", "aab"]))
    print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))


main()