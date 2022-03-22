class Queue:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []

    def enqueue(self, data):
        if self.items is not None:
            self.items.append(data)
            
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        
    def front(self):
        if not self.is_empty():
            return self.items[0]
    
    def rear(self):
        if not self.is_empty():
            return self.items[-1]
        
    def size(self):
        if self.items is not None:
            return len(self.items)
        
class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def push(self, data):
        if self.items is not None:
            self.items.append(data)
            
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        
    def size(self):
        if self.items is not None:
            return len(self.items)
        
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
        
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
        else:    
            queue = Queue()
            queue.enqueue(self.root)
            
            while queue.size() > 0:
                curr_node = queue.dequeue()
                
                if curr_node.left:
                    queue.enqueue(curr_node.left)
                else:
                    curr_node.left = new_node
                    return curr_node.left
                
                if curr_node.right:
                    queue.enqueue(curr_node.right)
                else:
                    curr_node.right = new_node
                    return curr_node
                
    def delete_node(self, data):
        if not self.root:
            return
        
        queue = Queue()
        queue.enqueue(self.root)
        
        while queue.size() > 0:
            curr_node = queue.dequeue()
            
            if curr_node.data == data:
                deepest_node = self.get_deepest_node()
                if curr_node is deepest_node:
                    self.root = None
                else:
                    curr_node.data = deepest_node.data
                    self.delete_deepest_node(deepest_node)
                return True
                
            if curr_node.left:
                queue.enqueue(curr_node.left)
                
            if curr_node.right:
                queue.enqueue(curr_node.right)
                    
    def get_deepest_node(self):
        if not self.root:
            return
        queue = Queue()
        queue.enqueue(self.root)
        
        while queue.size() > 0:
            curr_node = queue.dequeue()
            
            if curr_node.left:
                queue.enqueue(curr_node.left)
                
            if curr_node.right:
                queue.enqueue(curr_node.right)
        
        return curr_node
    
    def delete_deepest_node(self, deepest_node):
        if not self.root:
            return
        
        queue = Queue()
        queue.enqueue(self.root)
        
        while queue.size() > 0:
            curr_node = queue.dequeue()
            
            if curr_node is deepest_node:
                curr_node = None
                return True
                
            if curr_node.left:
                if curr_node.left is deepest_node:
                    curr_node.left = None
                    return True
                else:
                    queue.enqueue(curr_node.left)
            
                
            if curr_node.right:
                if curr_node.right is deepest_node:
                    curr_node.right = None
                    return True
                else:
                    queue.enqueue(curr_node.right)
           
                
        return False
    
    def pre_order_traversal(self, node):
        if not node:
            return
        
        print(node.data)
        self.pre_order_traversal(node.left)
        self.pre_order_traversal(node.right)
    
    def inorder_traversal(self, node):
        if not node:
            return
        
        self.inorder_traversal(node.left) 
        print(node.data)   
        self.inorder_traversal(node.right) 
        
    def post_order_traversal(self, node):
        if not node:
            return
        
        self.post_order_traversal(node.left)
        self.post_order_traversal(node.right)
        print(node.data)
     
    def level_order_traversal(self, node):
        if not node:
            return
        
        queue = Queue()
        queue.enqueue(node)
        
        while queue.size() > 0:
            print(queue.front().data)
            curr_node = queue.dequeue()
            
            if curr_node.left:
                queue.enqueue(curr_node.left)
            if curr_node.right:
                queue.enqueue(curr_node.right)
        
    def reverse_level_order_traversal(self, node):
        if not node:
            return
        
        stack = Stack()
        queue = Queue()
        queue.enqueue(node)
        
        while queue.size() > 0:
            curr_node = queue.dequeue()
            stack.push(curr_node.data)
            
            if curr_node.right:
                queue.enqueue(curr_node.right)
            
            if curr_node.left:
                queue.enqueue(curr_node.left)
                
        while stack.size() > 0:
            print(stack.pop())
     
    def height(self, node):
        if not node:
            return -1
        
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        
        return 1 + max(left_height, right_height)
                        
    def size_recursive(self, node):
        if not node:
            return 0
        
        left_count = self.size_recursive(node.left)       
        right_count = self.size_recursive(node.right) 
        
        return 1 + left_count + right_count    
    
    def size_iter(self):
        if self.root is None:
            return 0
        
        size = 0
        stack = Stack()
        stack.push(self.root)
        
        size += 1
        
        while stack.size() > 0:
            curr_node = stack.pop()
            
            if curr_node.left:
                size += 1
                stack.push(curr_node.left)
                
            if curr_node.right:
                size += 1
                stack.push(curr_node.right)
        
        return size       
         
tree = BinaryTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
# tree.delete_node(2)
# tree.delete_node(3)
# tree.delete_node(5)
# tree.delete_node(1)
# tree.delete_node(4)
# tree.delete_node(6)


# tree.pre_order_traversal(tree.root)
tree.inorder_traversal(tree.root)
# tree.post_order_traversal(tree.root)
# tree.level_order_traversal(tree.root)
# tree.reverse_level_order_traversal(tree.root)
# print(tree.height(tree.root))
# print(tree.size_recursive(tree.root))
# print(tree.size_iter())
