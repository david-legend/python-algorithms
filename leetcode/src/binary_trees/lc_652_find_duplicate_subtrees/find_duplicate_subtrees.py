def findDuplicateSubtrees(root):
    def findDups(node):
        if node is None: return "#"

        path = [str(node.val)]
        path.append(findDups(node.left))
        path.append(findDups(node.right))
        
        path = ",".join(path)
        if path in tree_map:
            tree_map[path] += 1
            if tree_map[path] == 2:
                result.append(node)
        else:
            tree_map[path] = 1
        
        return path
    
    result, tree_map = [], {}
    findDups(root)
    
    return result