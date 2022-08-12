# Add Credits

<br>

Consider a server that a large number of clients connect to. Each client is identified by a string. Each client has a "credit", which is a nonnegative integer value. 
The server needs to maintain a data structure to which clients can be added, removed, queried, or updated. 
In addition, the server needs to be able to add a specified number of credits to all clients simultaneously.

<br>

Design a data structure that implements the following methods:
- Insert: add a client with specified credit, replacing any existing entry for the client.
- Remove: delete the specified client.
- Lookup: return the number of credits associated with the specified client.
- Add-to-all: increment the credit count for all current clients by the specified amount. o Max: retum a client with the highest number of credits.
- Max: retum a client with the highest number of credits.

<br>

- Hint: Use additional global state.

<br>

### Example
- Insert('a', 4)  ---> Structure {(a,4)}
- Insert('b', 2)  ---> Structure {(a,4), (b,2)}
- Insert('c', 1)  ---> Structure {(a,4), (b,2), (c, 1)}
- Remove('c')  ---> Structure {(a,4), (b,2)}   
- LookUp('c')  ---> -1   
- LookUp('a')  ---> 4  
- AddAll(3)  ---> Structure {(a,7), (b,5)}  
- LookUp('a')  ---> 7 
- LookUp('b')  ---> 5 
- LookUp('b')  ---> 5 
- Max()  ---> 'a' 









