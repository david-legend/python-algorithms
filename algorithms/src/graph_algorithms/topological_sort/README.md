# Topological Sort

Topological sorting of vertices of a Directed Acyclic Graph is an ordering of the vertices V1, V2, ... Vn, in such a way,   
that if there is an edge directed towards vertex Vj from vertex Vi, then Vi comes before Vj. For example consider the graph given below:  

![Top Sort graph](https://he-s3.s3.amazonaws.com/media/uploads/d6be27e.png)

<br>

A topological sorting of this graph is: 1 2 3 4 5  
There are multiple topological sorting possible for a graph. For the graph given above one another topological sorting is: 1 2 3 4 5  
In order to have a topological sorting the graph must not contain any cycles. So topological sorting can be achieved for only directed and acyclic graphs.

<br>


[▶ Kahn's Algorithm | Topological Sort Algorithm | BFS Explanation](https://www.youtube.com/watch?v=73sneFXuTEg&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=23)
[▶ Topological Sort Algorithm | DFS Explanation](https://www.youtube.com/watch?v=5lZ0iJMrUMk&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=23)


## How it Works

Le'ts see how we can find a topological sorting in a graph. So basically we want to find a permutation of the vertices in which for every vertex 
Vi, all the vertices Vj having edges coming out and directed towards Vi comes before Vi.  

We'll maintain an array T that will denote our topological sorting. So, let's say for a graph having N vertices, we have an array indegree[]
of size N whose ith element tells the number of vertices which are not already inserted in T and there is an edge from them incident on vertex numbered i.  

We'll append vertices Vito the array T, and when we do that we'll decrease the value of indegree[Vj] by 1
for every edge from Vi to Vj. Doing this will mean that we have inserted one vertex having edge directed towards Vj.  
So at any point we can insert only those vertices for which the value of indgree[] is 0.  
The algorithm using a BFS traversal is given below:

```
topological_sort(N, adj[N][N])
    T = []
    visited = []
    in_degree = []
    for i = 0 to N
            in_degree[i] = visited[i] = 0

    for i = 0 to N
            for j = 0 to N
                    if adj[i][j] is TRUE
                            in_degree[j] = in_degree[j] + 1

    for i = 0 to N
            if in_degree[i] is 0
                    enqueue(Queue, i)
                    visited[i] = TRUE

    while Queue is not Empty
            vertex = get_front(Queue)
            dequeue(Queue)
            T.append(vertex)
            for j = 0 to N
                    if adj[vertex][j] is TRUE and visited[j] is FALSE
                            in_degree[j] = in_degree[j] - 1
                            if in_degree[j] is 0
                                    enqueue(Queue, j)
                                    visited[j] = TRUE
    return T
```


<br>

## Creating Minimum Spanning Tree Using Kruskal Algorithm

Let's take a graph and see the algorithm in action. Consider the graph given below:
<br>

![Step 1](https://he-s3.s3.amazonaws.com/media/uploads/0c3320c.png)

<br>

Initially indegre[0] == 0 and T is empty

<br>

![Step 2](https://he-s3.s3.amazonaws.com/media/uploads/401c3c4.png)

<br>

So, we delete 0 from Queue and append it to T. The vertices directly connected to 0 are 1 and 2 so we decrease their indegree[1] by 1. So, now indegree[1] = 0 and so 1 is pushed in Queue.

<br>

![Step 3](https://he-s3.s3.amazonaws.com/media/uploads/4aed1a4.png)

<br>

Next we delete 1 from Queue and append it to T. Doing this we decrease indegree[2] by 1, and now it becomes 0 and 2 is pushed into Queue.

<br>

![Step 4](https://he-s3.s3.amazonaws.com/media/uploads/54d23c8.png)

<br>

So, we continue doing like this, and further iterations looks like as follows:

<br>

![Step 5](https://he-s3.s3.amazonaws.com/media/uploads/ccb8663.png)


<br>

So at last we get our Topological sorting in T i.e. : 0 1 2 3 4 5  


### BFS Solution

Solution using a DFS traversal, unlike the one using BFS, does not need any special indegree[] array. Following is the pseudo code of the DFS solution:

```
T = []
visited = []

topological_sort( cur_vert, N, adj[][] ){
    visited[cur_vert] = true
    for i = 0 to N
        if adj[cur_vert][i] is true and visited[i] is false
        topological_sort(i)
    T.insert_in_beginning(cur_vert)
}
```

The following image of shows the state of stack and of array T in the above code for the same graph shown above.

![Stack](https://he-s3.s3.amazonaws.com/media/uploads/d43fba2.png)