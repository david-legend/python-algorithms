# Bellman–Ford Algorithm

The Bellman–Ford algorithm is an algorithm that computes shortest paths from a single source vertex to all of the other vertices in a weighted digraph.   
It is slower than Dijkstra's algorithm for the same problem, but more versatile, as it is capable of handling graphs in which some of the edge weights are negative numbers.
Negative edge weights are found in various applications of graphs, hence the usefulness of this algorithm. 

[▶ Bellman–Ford Algorithm Explanation](https://www.youtube.com/watch?v=0vVofAhAYjc&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=42)

<br> 
Here are some examples:
1. Can be used to explain a lot ofphenomena like cashflow, the heat released/absorbed in a chemical reaction, etc.

```
For instance, if there are different ways to reach from one chemical A to another chemical B, 
each method will have sub-reactions involving both heat dissipation and absorption.

If we want to find the set of reactions where minimum energy is required, 
then we will need to be able to factor in the heat absorption as negative weights and heat dissipation as positive weights.
```

### NOTE

1. The time complexity is O(VE)
2. Bellman–Ford Algorithm can handle graphs in which edges have negative weights.
3. If a graph contains a "negative cycle" (i.e. a cycle whose edges sum to a negative value), the Bellman–Ford algorithm can detect and report the negative cycle.

## Algorithmm

<br>

1. Start with a weighted graph

![Start with a weighted graph](https://cdn.programiz.com/sites/tutorial2program/files/Bellman-Ford-Algorithm-1.png)


<br>

2. Choose a starting vertex and assign infinity path values to all other vertices

![Choose a starting vertex and assign infinity path values to all other devices](https://cdn.programiz.com/sites/tutorial2program/files/Bellman-Ford-Algorithm-2.png)


<br>

3. Visit each edge and relax the path distances if they are inaccurate

![Visit each edge and relax the path distances if they are inaccurate](https://cdn.programiz.com/sites/tutorial2program/files/Bellman-Ford-Algorithm-3.png)


<br>

4. We need to this V times because in the worst case, a vertex's path length might need to be readjusted V times

![Choose a starting vertex and assign infinity path values to all other devices](https://cdn.programiz.com/sites/tutorial2program/files/Bellman-Ford-Algorithm-4.png)


<br>

5. Notice how the vertex at the top right corner had its path length adjusted

![Choose a starting vertex and assign infinity path values to all other devices](https://cdn.programiz.com/sites/tutorial2program/files/Bellman-Ford-Algorithm-5.png)


<br>

6. After all the vertices have their path lengths, we check if a negative cycle is present

![Choose a starting vertex and assign infinity path values to all other devices](https://cdn.programiz.com/sites/tutorial2program/files/Bellman-Ford-Algorithm-6.png)


<br><br><br>

### Pseudocode

- We need to maintain the path distance of every vertex. We can store that in an array of size v, where v is the number of vertices.

- We also want to be able to get the shortest path, not only know the length of the shortest path. For this, we map each vertex to the vertex that last updated its path length.

- Once the algorithm is over, we can backtrack from the destination vertex to the source vertex to find the path.

<br>

```
function bellmanFord(G, S)
  for each vertex V in G
    distance[V] <- infinite
      previous[V] <- NULL
  distance[S] <- 0

  for each vertex V in G				
    for each edge (U,V) in G
      tempDistance <- distance[U] + edge_weight(U, V)
      if tempDistance < distance[V]
        distance[V] <- tempDistance
        previous[V] <- U

  for each edge (U,V) in G
    If distance[U] + edge_weight(U, V) < distance[V}
      Error: Negative Cycle Exists

  return distance[], previous[]
```

<br><br><br>

### Bellman Ford vs Dijkstra

Bellman Ford's algorithm and Dijkstra's algorithm are very similar in structure. While Dijkstra looks only to the immediate neighbors of a vertex, Bellman goes through each edge in every iteration.

<br>

![Bellman Ford's Algorithm vs Dijkstra's Algorithm](https://cdn.programiz.com/sites/tutorial2program/files/bellman-ford-vs-dijkstra.jpg)