# Pattern 1: Sliding Window

In many problems dealing with an array (or a LinkedList), we are asked to find or 
calculate something among all the contiguous subarrays (or sublists) of a given size. 

For example, take a look at this problem:

Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

Let’s understand this problem with a real input:

Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5

A brute-force algorithm will calculate the sum of every 5-element 
contiguous subarray of the given array and divide the sum by ‘5’ to find the average.

The efficient way to solve this problem would be to visualize each contiguous subarray 
as a sliding window of ‘5’ elements. This means that we will slide the window by one element 
when we move on to the next subarray. To reuse the sum from the previous subarray, 
we will subtract the element going out of the window and add the element now being included in the sliding window. 
This will save us from going through the whole subarray to find the sum and, 
as a result, the algorithm complexity will reduce to O(N).

