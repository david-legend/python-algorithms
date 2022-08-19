

# Time O(1) | Space O(1)
# assumes node is not the tail
def delete_node(node_to_be_deleted):
    node_to_be_deleted.data = node_to_be_deleted.next.data
    node_to_be_deleted.next = node_to_be_deleted.next.next