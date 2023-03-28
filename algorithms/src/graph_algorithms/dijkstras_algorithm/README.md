# Dijkstra's Algorithmm

Dijkstra's algorithm (/ˈdaɪkstrəz/ DYKE-strəz) is an algorithm for finding the shortest paths between nodes in a weighted graph,.  

For a given source node in the graph, the algorithm finds the shortest path between that node and every other.  
It can also be used for finding the shortest paths from a single node to a single destination node by stopping the algorithm once the shortest path to the destination node has been determined.

[▶ Dijkstra's Algorithm - Using Priority Queue](https://www.youtube.com/watch?v=V6H1qAeB-l4&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=33)
<br>

[▶ Dijkstra's Algorithm - Using Set](https://www.youtube.com/watch?v=PATgNiuTP20&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=34)
<br>

[▶ Dijkstra's Algorithm - Why PQ and not Q, Intuition, Time Complexity Derivation](https://www.youtube.com/watch?v=3dINsjyfooY&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=35)
<br>

[▶ Print Shortest Path - Dijkstra's Algorithm](https://www.youtube.com/watch?v=rp1SMw7HSO8&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=36)
<br>


### NOTE

1. The time complexity is O(E logV). (See Proof In Implementation)
2. Dijkstra's algorithm but may or may not work with graphs in which edges have negative weights.
3. If a Graph has a negative cycle the Dijkstra's algorithm runs into an infinite loop.

## Algorithmm

<br>

1. Start with a weighted graph

![Start with a weighted graph](https://cdn.programiz.com/sites/tutorial2program/files/dj-1.png)


<br>

2. Choose a starting vertex and assign infinity path values to all other vertices

![Choose a starting vertex and assign infinity path values to all other vertices](https://cdn.programiz.com/sites/tutorial2program/files/dj-2.png)


<br>

3. Go to each vertex and update its path length

![Go to each vertex and update its path length](https://cdn.programiz.com/sites/tutorial2program/files/dj-3.png)


<br>

4. If the path length of the adjacent vertex is lesser than new path length, don't update it

![If the path length of the adjacent vertex is lesser than new path length, don't update it](https://cdn.programiz.com/sites/tutorial2program/files/dj-4.png)


<br>

5. Avoid updating path lengths of already visited vertices

![Avoid updating path lengths of already visited vertices](https://cdn.programiz.com/sites/tutorial2program/files/dj-5.png)


<br>

6. After each iteration, we pick the unvisited vertex with the least path length. So we choose 5 before 7

![After each iteration, we pick the unvisited vertex with the least path length. So we choose 5 before 7](https://cdn.programiz.com/sites/tutorial2program/files/dj-6.png)


<br>

7. Notice how the rightmost vertex has its path length updated twice

![Notice how the rightmost vertex has its path length updated twice](https://cdn.programiz.com/sites/tutorial2program/files/dj-7.png)


<br>

8. Repeat until all the vertices have been visited

![Repeat until all the vertices have been visited](https://cdn.programiz.com/sites/tutorial2program/files/dj-8.png)


<br><br><br>

### Pseudocode

- We need to maintain the path distance of every vertex. We can store that in an array of size v, where v is the number of vertices.

- We also want to be able to get the shortest path, not only know the length of the shortest path. For this, we map each vertex to the vertex that last updated its path length.

- Once the algorithm is over, we can backtrack from the destination vertex to the source vertex to find the path.

- A minimum priority queue can be used to efficiently receive the vertex with least path distance.

<br>

```
function dijkstra(G, S)
    for each vertex V in G
        distance[V] <- infinite
        previous[V] <- NULL
        If V != S, add V to Priority Queue Q
    distance[S] <- 0
	
    while Q IS NOT EMPTY
        U <- Extract MIN from Q
        for each unvisited neighbour V of U
            tempDistance <- distance[U] + edge_weight(U, V)
            if tempDistance < distance[V]
                distance[V] <- tempDistance
                previous[V] <- U
    return distance[], previous[]
```

<br><br><br>

### Bellman Ford vs Dijkstra

Bellman Ford's algorithm and Dijkstra's algorithm are very similar in structure. While Dijkstra looks only to the immediate neighbors of a vertex, Bellman goes through each edge in every iteration.

<br>

![Bellman Ford's Algorithm vs Dijkstra's Algorithm](https://cdn.programiz.com/sites/tutorial2program/files/bellman-ford-vs-dijkstra.jpg)