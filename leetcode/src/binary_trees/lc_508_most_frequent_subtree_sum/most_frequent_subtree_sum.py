from collections import defaultdict

# Solution 1 - Use Two Maps 
# Time O(n) | Space O(n)
def findFrequentTreeSum(root):
    def treeSumHelper(node):
        nonlocal max_count
        if node is None: return 0
        
        left = treeSumHelper(node.left)
        right = treeSumHelper(node.right)
        
        subtree_sum = node.val + left + right
        sum_to_count[subtree_sum] += 1
        
        count_to_sums[sum_to_count[subtree_sum]].append(subtree_sum)
        max_count = max(max_count, sum_to_count[subtree_sum])
        
        return subtree_sum
        
    
    sum_to_count, count_to_sums = defaultdict(int), defaultdict(list)
    max_count = 0
    treeSumHelper(root)
    
    return count_to_sums[max_count]


# Solution 2  - Use Only One Map 
# Time O(n) | Space O(n)
def findFrequentTreeSum2(root):
    def treeSumHelper(node):
        nonlocal max_count
        if node is None: return 0
        
        left = treeSumHelper(node.left)
        right = treeSumHelper(node.right)
        
        subtree_sum = node.val + left + right
        sum_to_count[subtree_sum] += 1
        
        max_count = max(max_count, sum_to_count[subtree_sum])
        
        return subtree_sum
        
    sum_to_count, max_count, result = defaultdict(int), 0 , []
    treeSumHelper(root)
    
    for subtree_sum, count in sum_to_count.items():
        if count == max_count:
            result.append(subtree_sum)
    
    return result