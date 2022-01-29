from heapq import *

# Time complexity
# Since, at the most, all the projects will be pushed to both the heaps once, 
# the time complexity of our algorithm is O(NlogN + KlogN), 
# where ‘N’ is the total number of projects and ‘K’ is the number of projects we are selecting.
# 
# Space complexity
# The space complexity will be O(N) because 
# we will be storing all the projects in the heaps.

def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    min_capital_heap = []
    max_profit_heap = []
    
    for i in range(len(capital)):
        heappush(min_capital_heap, (capital[i], i))
    
    available_capital = initialCapital
    for _ in range(numberOfProjects):
        while min_capital_heap and available_capital >= min_capital_heap[0][0]:
            cap, i = heappop(min_capital_heap)
            heappush(max_profit_heap, (-profits[i], i))
            
        if not max_profit_heap:
            break
        
        available_capital += -heappop(max_profit_heap)[0]
        
    return available_capital


print("Maximum capital: " +
    str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
print("Maximum capital: " +
    str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


