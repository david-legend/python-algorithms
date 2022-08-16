# Compute Median From A Stream

You want to compute the running median of a sequence of numbers. The sequence is presented to you in a streaming fashion-you 
cannot back up to read an earlier value, and you need to output the median after reading in each new element. 
For example, if the input is 1,0,3,5,2,0,1 the output is 1, 0.5, 1, 2, 2, 1.5, 1

<br>

Design an algorithm for computing the running median of a sequence.

<br>

### Example 1
- input:  [1,0,3,5,2,0,1]
- output: [1,0.5,1,2,2,1.5,1]


### Example 2
- input:  [11,10,31,52,2,7,1]
- output: [11, 10.5, 11, 21.0, 11, 10.5, 10]