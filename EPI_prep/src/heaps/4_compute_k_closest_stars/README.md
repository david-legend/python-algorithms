# Compute The K Closest Stars


Consider a coordinate system for the Milky Way, in which Earth is at (0,0,0). Model stars as points, and assume distances are in light years. 
The Milky Way consists of approximately 1012 stars, and their coordinates are stored in a file.
How would you compute the k stars which are closest to Earth? 

<br>

- Suppose you know the k closest stars in the first r stars. If the (r + 1.)th star is to be added to the set of k closest stars, which element in that set should be evicted?

<br>

<br>

### Example 1
- input:  [Star(1,1,1), Star(0, 0, 1), Star(0, 1, 0), Star(2,2,2), Star(1,2,1)], k = 2
- output: [(0, 0, 1), (0, 1, 0)]

### Example 2
- input:  [Star(1,1,1), Star(0, 0, 1), Star(0, 1, 0), Star(2,2,2), Star(1,2,1)], k = 3
- output: [(0, 0, 1), (0, 1, 0), (1, 1, 1)]

