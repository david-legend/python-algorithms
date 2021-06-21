# We are given an array A consisting of N integers. In one move, we can choose any element in this array 
# and replace it with any value. What is the smallest possible amplitude of array A that we can achieve 
# by performing at most three moves? The amplitude of an array is the difference between the largest and 
# the smallest values it contains.


# Write a function:
# class Solution (public int solution(int[] A); }
# that, given an array A of N integers, returns the smallest amplitude that can be obtained after 
# smallest amplitude that can be obtained after replacing up to three elements of array A.

#Examples:
#
#1. Given A = [-9, 8, -1], the function should return We can replace -9 and 8 
# with -1 so that all elements are equal to -1, and then the amplitude is 0.
#
#2. Given A = [14, 10, 5, 1, 0], the function should return 1. To achieve an amplitude of 1,
#  we can replace 14, 10 and 5 with 1 or 0.
#
#3. Given A = [11, 0, -6, -1, -3, 5], the function should return 3. 
# This can be achieved, for example, by replacing 11, -6 and 5 with three values of -2.
#
#4. Given A = [10, 10, -6, 2, -3, 10], the function should return O. We can replace -6, 2 and -3
#should return O. We can replace -6, 2 and -3 with 10, making the amplitude equal to 0.
#
#5. Given A = [8,-1, 4, 3, 5, -1], the function should return 2.
# Replacing 8 and both occurrences of -1 with, for example, 3, 4 and 5 results in an amplitude equal to 2.
#
#Assume that:
#N is an integer within the range [2..12]; • each element of array A is an integer within the range [-50..50].
#
#In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.