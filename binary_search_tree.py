class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key
        self.value = None

    def __repr__(self):
        return f'({self.key}, {self.value})'

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # O(n) or or O(log n) O(h) - height of tree
    def __contains__(self, key):
        current_node = self.root

        while current_node is not None:
            if key < current_node.key:
                current_node = current_node.left
            elif key > current_node.key:
                current_node = current_node.right
            else:
                return True
        return False
    
    # O(n)
    def __iter__(self):
        yield from self._in_order_traversal(self.root)

    # O(n)
    def __repr__(self):
        return str(list(self._in_order_traversal(self.root)))

    # O(n) or or O(log n) O(h) - height of tree
    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key)
            self.root.value = value
        else:
            current_node = self.root
            while True:
                if key < current_node.key:
                    if current_node.left is None:
                        current_node.left = Node(key)
                        current_node.left.value = value
                        current_node.left.parent = current_node
                        break
                    else:
                        current_node = current_node.left
                elif key > current_node.key:
                    if current_node.right is None:
                        current_node.right = Node(key)
                        current_node.right.value = value
                        current_node.right.parent = current_node
                        break
                    else:
                        current_node = current_node.right
                else:
                    current_node.value = value
                    break

    # O(n) or or O(log n) O(h) - height of tree
    def search(self, key):
        current_node = self.root

        while True:
            if current_node is None or current_node.key == key:
                return current_node
            elif key < current_node.key:
                if current_node.left is None:
                    return None
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    return None
                else:
                    current_node = current_node.right

    # O(n) or or O(log n) O(h) - height of tree
    def delete(self, key):
        node = self.search(key)

        if node is None:
            raise KeyError('Node with this key not found')
        
        self._delete(node)

    # O(n)
    def traverse(self, order = 'in'):
        if order == 'in':
            yield from self._in_order_traversal(self.root)
        elif order == 'pre':
            yield from self._pre_order_traversal(self.root)
        elif order == 'post':
            yield from self._post_order_traversal(self.root)
        else:
            raise ValueError('Unknown order')

    def _delete(self, node):
        if node.left is None and node.right is None:
            if node.parent is None:
                self.root = None
            else:
                if node.parent.right == node:
                    node.parent.right = None
                else:
                    node.parent.left = None
                node.parent = None
        elif node.left is None or node.right is None:
            child_node = node.left if node.left is not None else node.right

            if node.parent is None:
                child_node.parent = None
                self.root = child_node
            else:
                if node.parent.right == node:
                    node.parent.right = child_node
                else:
                    node.parent.left = child_node
                child_node.parent = node.parent
            
            node.parent = node.left = node.right = None

        else:
            successor = self._successor(node)

            node.key = successor.key
            node.value = successor.value

            self._delete(successor)

    def _successor(self, node):
        if node is None:
            raise ValueError("Successor not found")
        
        if node.right is None:
            return None
        else:
            current_node = node.right

            while current_node.left is not None:
                current_node = current_node.left
            return current_node

    def _predecessor(self, node):
        if node is None:
            raise ValueError("Predecessor not found")
        
        if node.left is None:
            return None
        else:
            current_node = node.left

            while current_node.right is not None:
                current_node = current_node.right
            return current_node

    def _in_order_traversal(self, node):
        if node is not None:
            yield from self._in_order_traversal(node.left)
            yield (node.key, node.value)
            yield from self._in_order_traversal(node.right)

    def _pre_order_traversal(self, node):
        if node is not None:
            yield (node.key, node.value)
            yield from self._pre_order_traversal(node.left)
            yield from self._pre_order_traversal(node.right)

    def _post_order_traversal(self, node):
        if node is not None:
            yield from self._pre_order_traversal(node.left)
            yield from self._pre_order_traversal(node.right)
            yield (node.key, node.value)

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10, 'test')
    bst.insert(15, 'test')
    bst.insert(12, 'test')
    bst.insert(17, 'test')
    bst.insert(25, 'test')
    bst.insert(5, 'test')
    # bst.delete(10)
    traverse = bst.traverse('pre')
    for i in traverse:
        print(i)
    print(bst.search(25))