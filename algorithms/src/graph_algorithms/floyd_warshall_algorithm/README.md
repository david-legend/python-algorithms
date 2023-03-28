# Floyd Warshall Algorithmm

Floyd-Warshall Algorithm is an algorithm for finding the shortest path between all the pairs of vertices in a weighted graph.   
This algorithm works for both the directed and undirected weighted graphs. But, it does not work for the graphs with negative cycles (where the sum of the edges in a cycle is negative).

```
A weighted graph is a graph in which each edge has a numerical value associated with it.
```

This algorithm follows the dynamic programming approach to find the shortest paths.

[▶ Floyd Warshall Algorithm Explanation](https://www.youtube.com/watch?v=YbY8cVwWAvw&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=43)

<br>

## How Floyd-Warshall Algorithm Works ?

Let the given graph be:  

<br>

![Initial graph](https://cdn.programiz.com/sites/tutorial2program/files/fw-Graph.png)

<br>

Follow the steps below to find the shortest path between all the pairs of vertices.  
### Step 1

Create a matrix A0 of dimension n*n where n is the number of vertices. The row and the column are indexed as i and j respectively. i and j are the vertices of the graph.  

Each cell A[i][j] is filled with the distance from the ith vertex to the jth vertex. If there is no path from ith vertex to jth vertex, the cell is left as infinity.

<br>    

![Fill each cell with the distance between ith and jth vertex](https://cdn.programiz.com/sites/tutorial2program/files/fw-Matrix-1.png)

<br>  

### Step 2

Now, create a matrix A1 using matrix A0. The elements in the first column and the first row are left as they are. The remaining cells are filled in the following way.  

Let k be the intermediate vertex in the shortest path from source to destination. In this step, k is the first vertex. A[i][j] is filled with (A[i][k] + A[k][j]) if (A[i][j] > A[i][k] + A[k][j]).  

That is, if the direct distance from the source to the destination is greater than the path through the vertex k, then the cell is filled with A[i][k] + A[k][j].  

In this step, k is vertex 1. We calculate the distance from source vertex to destination vertex through this vertex k.  

<br>  

![Calculate the distance from the source vertex to destination vertex through this vertex k](https://cdn.programiz.com/sites/tutorial2program/files/fw-Matrix-2.png)

<br>

For example: For A1[2, 4], the direct distance from vertex 2 to 4 is 4 and the sum of the distance from vertex 2 to 4 through vertex (ie. from vertex 2 to 1 and from vertex 1 to 4) is 7. Since 4 < 7, A0[2, 4] is filled with 4.

<br><br>

### Step 3

Similarly, A2 is created using A1. The elements in the second column and the second row are left as they are.  

In this step, k is the second vertex (i.e. vertex 2). The remaining steps are the same as in step 2.  

<br>  

![Calculate the distance from the source vertex to destination vertex through this vertex 2](https://cdn.programiz.com/sites/tutorial2program/files/fw-Matrix-3.png)

<br>


### Step 4

Similarly, A3 and A4 is also created

<br>

![Calculate the distance from the source vertex to destination vertex through this vertex 3](https://cdn.programiz.com/sites/tutorial2program/files/fw-Matrix-4.png)

<br>

![Calculate the distance from the source vertex to destination vertex through this vertex 4](https://cdn.programiz.com/sites/tutorial2program/files/fw-Matrix-5.png)

<br>

A4 gives the shortest path between each pair of vertices.


<br><br>

## Floyd-Warshall Algorithm

```
n = no of vertices
A = matrix of dimension n*n
for k = 1 to n
    for i = 1 to n
        for j = 1 to n
            Ak[i, j] = min (Ak-1[i, j], Ak-1[i, k] + Ak-1[k, j])
return A
```

<br>

### Python Code

```
# Floyd Warshall Algorithm in python


# The number of vertices
nV = 4

INF = 999


# Algorithm implementation
def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(distance)


# Printing the solution
def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


G = [[0, 3, INF, 5],
         [2, 0, INF, 4],
         [INF, 1, 0, INF],
         [INF, INF, 2, 0]]
floyd_warshall(G)
```

<br><br>

## Floyd Warshall Algorithm Complexity

### Time Complexity

There are three loops. Each loop has constant complexities. So, the time complexity of the Floyd-Warshall algorithm is O(n3).

### Space Complexity

The space complexity of the Floyd-Warshall algorithm is O(n2).

<br>

## Floyd Warshall Algorithm Applications

- To find the shortest path is a directed graph
- To find the transitive closure of directed graphs
- To find the Inversion of real matrices
- For testing whether an undirected graph is bipartite