# Courses Scheduling Order (medium) ✩

 There are ‘N’ courses, labeled from ‘0’ to ‘N-1’. Each course has some prerequisite courses 
 which need to be completed before it can be taken. Given the number of courses and a list of 
 prerequisite pairs, write a method to find the best ordering of the courses that a 
 student can take in order to finish all courses.

### Example 1
Input: Courses=3, Prerequisites=[0, 1], [1, 2]
Output: [0, 1, 2]
Explanation: To complete course '1', course '0' needs to be completed first. Similarly, course '1' needs
to be completed before '2' can be scheduled. A possible scheduling of Courses is: [0, 1, 2] 


### Example 2
Input: Courses=3, Prerequisites=[0, 1], [1, 2], [2, 0]
Output: []
Explanation: The Courses have a cyclic dependency, therefore they cannot be scheduled.

### Example 3
Input: Courses=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: [0 1 4 3 2 5] 
Explanation: A possible scheduling of Courses is: [0 1 4 3 2 5] 
