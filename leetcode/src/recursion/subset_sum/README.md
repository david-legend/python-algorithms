<!-- <a name="687. Longest Univalue Path - Medium"></a> -->
# [Subset Sums- Medium](https://practice.geeksforgeeks.org/problems/subset-sums2234/1)

Given a list arr of N integers, print sums of all subsets in it.   

<br>

### Example 1
```
Input:
N = 2
arr[] = {2, 3}
Output:
0 2 3 5
Explanation:
When no elements is taken then Sum = 0.
When only 2 is taken then Sum = 2.
When only 3 is taken then Sum = 3.
When element 2 and 3 are taken then 
Sum = 2+3 = 5.
```


<br>

### Example 2
```
Input:
N = 3
arr = {5, 2, 1}
Output:
0 1 2 3 5 6 7 8
```

### Example 3
```
Input: arr = [5,1,3,4,2]
Output: 3
Explanation: We can reach the end from starting indices 1, 2, and 4.
```

### Constraints:

- 1 <= N <= 15
- 0 <= arr[i] <= 104