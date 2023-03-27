# Introduction to Kruskal Algorithm

Kruskal algorithm is used to generate a minimum spanning tree for a given graph.  

Kruskal’s algorithm is the concept that is introduced in the graph theory of discrete mathematics. It is used to discover the shortest path between two points in a connected weighted graph. This algorithm converts a given graph into the forest, considering each node as a separate tree.  

These trees can only link to each other if the edge connecting them has a low value and doesn’t generate a cycle in MST structure.

<br>

[▶ Kruskals Algorithm Explanation](https://www.youtube.com/watch?v=1KRmCzBl_mQ&list=PLgUwDviBIf0rGEWe64KWas0Nryn7SCRWw&index=25)

<br>

## Creating Minimum Spanning Tree Using Kruskal Algorithm

1. Step 1: Sort all edges in increasing order of their edge weights.
2. Step 2: Pick the smallest edge.
3. Step 3: Check if the new edge creates a cycle or loop in a spanning tree.
4. Step 4: If it doesn’t form the cycle, then include that edge in MST. Otherwise, discard it.
5. Step 5: Repeat from step 2 until it includes |V| - 1 edges in MST.

<br>


### Step 1

Using the steps mentioned above, lets generate a minimum spanning tree structure. Lets take a look at an example to understand this process better.  

The graph G(V, E) given below contains 6 vertices and 12 edges. And we will create a minimum spanning tree T(V’, E’) for G(V, E) such that the number of   
vertices in T will be 6 and edges will be 5 (6-1).

<br>


![Start with a weighted graph](https://www.simplilearn.com/ice9/free_resources_article_thumb/Kruskals_algorithm/Graph_for_Constructing_MST.png)

<br>

If you observe this graph, you’ll find two looping edges connecting the same node to itself again. And you know that the tree structure can never include a   
loop or parallel edge. Hence, primarily you will need to remove these edges from the graph structure.

<br>

![Start with a weighted graph](https://www.simplilearn.com/ice9/free_resources_article_thumb/Kruskals_algorithm/Removing_Loops-OR-Parallel_Edges.png)

<br><br>

The next step that you will proceed with is arranging all edges in a sorted list by their edge weights.

<br><br>

![Kruskals Sorted](../../../../assets/kruskals_sorted.png)



<br>
<br>

## Step 2

<br>

After this step, you will include edges in the MST such that the included edge would not form a cycle in your tree structure.  
The first edge that you will pick is edge EF, as it has a minimum edge weight that is 2.

<br>

![Edge_EF_Insertion](https://www.simplilearn.com/ice9/free_resources_article_thumb/Kruskals_algorithm/Edge_EF_Insertion.png)


<br>

Add edge FD to the spanning tree.

<br>

![Edge_DF_Insertion](https://www.simplilearn.com/ice9/free_resources_article_thumb/Kruskals_algorithm/Edge_DF_Insertion.png)

<br>

Add edge BC and edge CF to the spanning tree as it does not generate any loop.

<br>

![Edge_BCandCF_Insertion](https://www.simplilearn.com/ice9/free_resources_article_thumb/Kruskals_algorithm/Edge_BCandCF_Insertion.png)

<br>

Next up is edge CD. This edge generates the loop in Your tree structure. Thus, you will discard this edge

<br>

![Discarding_Edge_CD](https://www.simplilearn.com/ice9/free_resources_article_thumb/Kruskals_algorithm/Discarding_Edge_CD.png)

<br>

Following edge CD, you have edge BF. This edge also creates the loop; hence you will discard it.

<br>

![Discarding_Edge_BF](https://www.simplilearn.com/ice9/free_resources_article_thumb/Kruskals_algorithm/Discaeding_Edge_BF.png)

<br>

Next up is edge BD. This edge also formulates a loop, so you will discard it as well.

<br>

![Discarding_Edge_BD](https://www.simplilearn.com/ice9/free_resources_article_thumb/Kruskals_algorithm/Discarding_Edge_BD.png)

<br>

Next on your sorted list is edge AB. This edge does not generate any cycle, so you need not include it in the MST structure. By including this node, it will include 5 edges in the MST, so you don’t have to traverse any further in the sorted list. The final structure of your MST is represented in the image below:

<br>

![Kruskals_Algorithm-Minimum_Spanning_Tree](https://www.simplilearn.com/ice9/free_resources_article_thumb/Kruskals_algorithm/Kruskals_Algorithm-Minimum_Spanning_Tree.png)


<br><br>

The summation of all the edge weights in MST T(V’, E’) is equal to 17, which is the least possible edge weight for any possible spanning tree structure for this particular graph.  
Moving ahead, you will learn about implementing Kruskal algorithms using the Union Find Algorithm.


<br><br>

## What is Union Find Algorithm?

Union Find is an algorithm that keeps track of elements that are split into one or over one disjoint set. It has two primary operations: Find and Union. The Find operation returns the set of elements to which the given element (argument) belongs, whereas the Union operation merges two disjoint sets.  

You need to divide the provided graph G(V, E) into three separate sets while building the Minimum Spanning Tree using Kruskal's approach. The first contains edge weight values, the second has a tree hierarchy for distinct nodes, and the third includes the rank of all nodes. By using Union and Find operations, it joins the distinct nodes which are treated as different trees themselves to formulate a minimum spanning tree. 


<br><br>

## Implementation of Kruskal Algorithm

Any MST algorithm revolves around determining whether adding an edge would result in a loop or not. Union Find is the most popular algorithm for determining this. The Union-Find algorithm separates vertices into clusters, allowing you to determine whether two vertices belong to the same cluster and hence if adding an edge will produce a cycle.

The strategy to implement the Kruskal algorithm using Union-Find is given below:  

- Construct a structure to keep track of the source and destination nodes, as well as their weight.
- Sort all the edges of a graph according to their edge-weight values.
- Create three distinct sets to maintain nodes of a graph, their hierarchy in a tree, and corresponding ranks for every node.
- Primarily, initialize all rank values to 0 and parent values to -1 (representing each node as its own tree itself).
- For each insertion of an edge in MST, you will update the rank and parent of each node.
- Do not insert the edge connecting two nodes if they have the same parent node, as this will cause a cycle in the tree structure.

<br>

Now, you will understand this implementation strategy with the help of an example. The graph for which you will develop a minimum spanning tree using Kruskal’s approach is given below:

<br>

![Graph_for_Implementing_Kruskals_Algorithm](https://www.simplilearn.com/ice9/free_resources_article_thumb/Kruskals_algorithm/Graph_for_Implementing_Kruskals_Algorithm.png)

<br>

Initially, you will need to create two sets for maintaining parent value and rank value for each node. Along with that, you will create a structure to keep the edges of the graph. For all the nodes in the graph, you will initialize parent values to -1 and rank values to 0. The reason behind that is that you need to treat all the nodes of a graph as trees themselves.

<br>

![Initialising_Parent_and_Rank_set_values-Kruskals_Algorithm](https://www.simplilearn.com/ice9/free_resources_article_thumb/Kruskals_algorithm/Initialising_Parent_and_Rank_set_values-Kruskals_Algorithm.png)

<br>

Additionally, remember that whenever you join two disjoint tree structures together, the rank of one being pointed to will increase by one. So, once you add edges into the MST, the rank and parent values of included nodes will change. This particular graph will show the state of sets, like the figure below.

<br>

![Set_Updation-Kruskals_Algorithm](https://www.simplilearn.com/ice9/free_resources_article_thumb/Kruskals_algorithm/Set_Updation-Kruskals_Algorithm.png)