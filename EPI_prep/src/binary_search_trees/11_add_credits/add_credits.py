import bintrees


# Solution: 
# A hash table is a natural data structure for this problem. 
# However, it does not support efficient max operations, nor is there an 
# obvious way to perform the simultaneous increment, short traversing all entries. 
# A BST does have efficient max operation, but it too does not natively support the global increment.

# A general principle when adding behaviors to an object is to wrap the object, and add functions in the 
# wrapper which add behaviors before or after delegating to the object. In our context this suggests 
# storing the clients in a BST, and having the wrapper track the total increment amount.


# For example, if we have clients A, B, C, with credits 1.,2,3, respectively, and want to add 5 credits to each, 
# the wrapper sets the total increment amount to 5. A lookup on B then is performed by looking up in the BST, 
# which returns 2, and then adding 5 before returning. If we want to add 4 more credits to each, 
# we simply update the total increment amount to 9.

# One issue to watch out for is what happens to clients inserted after a call to the add-to-all function. 
# Continuing with the given example, if we were to now add D with a credit of 6, 
# the lookup would retum 6 + 9, which is an error.
# The solution is simple-subtract the increment from the credit, i.e., add D with a credit of 6 - 9 = -3 to the BST.
#  Now a lookup for D will retum -3 + 9, which is the correct amount.

# More specifically, the BST keys are credits, and the corresponding values are the clients with that credit. 
# This makes for fast max-queries. Howevet to perform lookups and removes by client quickly, 
# the BST by itself is not enough (since it is ordered by credit, not client id). 
# We can solve this by maintainig an additional hash table in which keys are clients, and values are credits. 
# Lookup is trivial. Removes entails a lookup in the hash to get the credit, and then a search into the BST to get 
# the set of clients with that credit, and finally a delete on that set.

class ClientsCreditInfo:
    def __init__(self):
        self._offset = 0
        self._client_to_credit = {}
        self._credit_to_clients = bintrees.RBTree()
    

    # Time O(logn) 
    # where n is the number of clients in the data structure
    def insert(self, client_id, credit):
        self.remove(client_id)
        offset_credit = credit - self._offset
        self._client_to_credit[client_id] = offset_credit
        self._credit_to_clients.set_default(offset_credit, set()).add(client_id)

    # Time O(logn) 
    # where n is the number of clients in the data structure
    def remove(self, client_id):
        credit = self._client_to_credit.get(client_id)

        if credit is not None:
            self._credit_to_clients[credit].remove(client_id)
            
            if not self._credit_to_clients[credit]:
                del self._credit_to_clients[credit]
            del self._client_to_credit[client_id]
            return True
        
        return False
    
    # Time O(1)
    def lookup(self, client_id):
        credit = self._client_to_credit.get(client_id)
        return credit + self._offset if credit is not None else -1
    
    # Time O(1)
    def add_to_all(self, credit):
        self._offset += credit
    
    #Library BST implementations uses caching to perform max in O(1) time
    def max(self):
        if not self._credit_to_clients:
            return ''
        
        clients = self._credit_to_clients.max_item()[1]
        return '' if not clients else next(iter(clients))


clientsInfo = ClientsCreditInfo()
clientsInfo.insert('a', 4)
clientsInfo.insert('b', 2)
clientsInfo.insert('c', 1)
clientsInfo.remove('c')
print(clientsInfo.lookup('c')) # -1 
print(clientsInfo.lookup('a')) # 4
clientsInfo.add_to_all(3)
print(clientsInfo.lookup('a')) # 7
print(clientsInfo.lookup('b')) # 5
print(clientsInfo.max()) # 'a'