# Course Scheduling (medium) ✩

There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks 
which need to be completed before it can be scheduled. Given the number of tasks and a 
list of prerequisite pairs, find out if it is possible to schedule all the tasks.

### Example 1
Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: true
Explanation: To take course '1', course '0' needs to be completed first. Similarly, course '1' needs 
to be completed before '2' can be taken. One possible scheduling of tasks is: [0, 1, 2] 


### Example 2
Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
Output: false
Explanation: The courses have a cyclic dependency, therefore they cannot be scheduled.

### Example 3
Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: true
Explanation: A possible scheduling of course is: [0 1 4 3 2 5]
