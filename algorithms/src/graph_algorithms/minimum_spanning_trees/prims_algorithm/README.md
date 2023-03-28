# Prim's Algorithm

Prim's algorithm is a minimum spanning tree algorithm that takes a graph as input and finds the subset of the edges of that graph which

- form a tree that includes every vertex
- has the minimum sum of weights among all the trees that can be formed from the graph


[▶ Prim's Algorithm Explanation](https://www.youtube.com/watch?v=mJcZjjKzeqk&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=45)

<br>

## How Prim's algorithm works

It falls under a class of algorithms called greedy algorithms that find the local optimum in the hopes of finding a global optimum.  

We start from one vertex and keep adding edges with the lowest weight until we reach our goal.  

The steps for implementing Prim's algorithm are as follows:  

- Initialize the minimum spanning tree with a vertex chosen at random.
- Find all the edges that connect the tree to new vertices, find the minimum and add it to the tree
- Keep repeating step 2 until we get a minimum spanning tree


## Example of Prim's algorithm

<br>

1. Start with a weighted graph

<br>

![Start with a weighted graph](https://cdn.programiz.com/sites/tutorial2program/files/pa_1.png)


<br>

2. Choose a vertex

<br>

![Choose a vertex](https://cdn.programiz.com/sites/tutorial2program/files/pa_2.png)

<br>

3. Choose the shortest edge from this vertex and add it

<br>

![Choose the shortest edge from this vertex and add it](https://cdn.programiz.com/sites/tutorial2program/files/pa_3.png)


<br>

4. Choose the nearest vertex not yet in the solution

<br>

![Choose the nearest vertex not yet in the solution](https://cdn.programiz.com/sites/tutorial2program/files/pa_4.png)


<br>

5. Choose the nearest edge not yet in the solution, if there are multiple choices, choose one at random

<br>

![Choose the nearest edge not yet in the solution, if there are multiple choices, choose one at random](https://cdn.programiz.com/sites/tutorial2program/files/pa_5.png)


<br>

6. Repeat until you have a spanning tree

<br>

![Repeat until you have a spanning tree](https://cdn.programiz.com/sites/tutorial2program/files/pa_6.png)


<br><br>

## Prim's Algorithm pseudocode

The pseudocode for prim's algorithm shows how we create two sets of vertices U and V-U. U contains the list of vertices that have been visited and V-U the list of vertices that haven't.  One by one, we move vertices from set V-U to set U by connecting the least weight edge.

```
T = ∅;
U = { 1 };
while (U ≠ V)
    let (u, v) be the lowest cost edge such that u ∈ U and v ∈ V - U;
    T = T ∪ {(u, v)}
    U = U ∪ {v}
```

<br>

Although adjacency matrix representation of graphs is used, this algorithm can also be implemented using Adjacency List to improve its efficiency.

```
# Prim's Algorithm in Python


INF = 9999999
# number of vertices in graph
V = 5
# create a 2d array of size 5x5
# for adjacency matrix to represent graph
G = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]
# create a array to track selected vertex
# selected will become true otherwise false
selected = [0, 0, 0, 0, 0]
# set number of edge to 0
no_edge = 0
# the number of egde in minimum spanning tree will be
# always less than(V - 1), where V is number of vertices in
# graph
# choose 0th vertex and make it true
selected[0] = True
# print for edge and weight
print("Edge : Weight\n")
while (no_edge < V - 1):
    # For every vertex in the set S, find the all adjacent vertices
    #, calculate the distance from the vertex selected at step 1.
    # if the vertex is already in the set S, discard it otherwise
    # choose another vertex nearest to selected vertex  at step 1.
    minimum = INF
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and G[i][j]):  
                    # not in selected and there is an edge
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
    selected[y] = True
    no_edge += 1
```

<br><br>

## Prim's vs Kruskal's Algorithm

Kruskal's algorithm is another popular minimum spanning tree algorithm that uses a different logic to find the MST of a graph.   
Instead of starting from a vertex, Kruskal's algorithm sorts all the edges from low weight to high and keeps adding the lowest edges, ignoring those edges that create a cycle.

<br>

## Prim's Algorithm Complexity

The time complexity of Prim's algorithm is O(E log V).

<br>

## Prim's Algorithm Application

- Laying cables of electrical wiring
- In network designed
- To make protocols in network cycles