from collections import deque


class BinarySearchTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        # we can not have duplicate values in binary tree 
        if data == self.data:
            return 
        
        # if value is smaller than current data
        if data < self.data:
            # Add in left side
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        
        # else should be add at right side
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):

        elements = []

        # get all the left element in array and append it in list
        if self.left:
            elements += self.left.in_order_traversal()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()


        return elements

    def iterative_in_orderTraversal(self, root):
        
        current = root

        stack, tree = [], []

        while True:

            if current:
                stack.append(current)
                current = current.left

            elif stack:
                current = stack.pop()
                tree.append(current.data)
                current = current.right        

            else:
                break

        return tree
    
    def pre_order_traversal(self):

        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()
        
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
    
    def iterative_pre_order_traversal(self, root):
        
        current = root

        tree, stack = [], []

        while True:
            if current:
                tree.append(current.data)
                stack.append(current)
                current = current.left
            
            elif stack:
                current = stack.pop()
                current = current.right
            
            else:
                break

        return tree

    def post_order_traversal(self):

        elements = []

        if self.left:
            elements += self.left.post_order_traversal()
        
        if self.right:
            elements += self.right.post_order_traversal()
        
        elements.append(self.data)

        return elements
    
    def iterative_post_order_traversal(self, root):

        stack, out = deque(), deque()

        stack.append(root)

        while stack:

            curr = stack.pop()
            out.append(curr.data)

            if curr.left:
                stack.append(curr.left)
            
            if curr.right:
                stack.append(curr.right)

        while out:
            print(out.pop())

    def search(self, data):

        if self.data == data:
            return True
        
        elif data < self.data:

            if self.left:
                return self.search(data)
            else:
                return False

        elif data > self.data:
            if self.right:
                return self.search(data)
            else:
                return False

        else:
            return False

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def level_order_traversal(self, root):
        if not root:
            return 
        
        queue = []
        lot = []

        queue.append(root)

        while queue:

            current = queue.pop(0)
            lot.append(current.data)

            if current.left:
                queue.append(current.left)
            
            if current.right:
                queue.append(current.right)
        
        return lot

def build_binary_tree(elements):
    
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

def traversal_algo(number_tree):
    # in_order_tree = numbers_tree.in_order_traversal()
    # iterative_in_order_traversal = numbers_tree.iterative_in_orderTraversal(numbers_tree)
    # pre_order_tree = numbers_tree.pre_order_traversal()
    # iterative_pre_order_traversal = numbers_tree.pre_order_traversal()
    # post_order_tree = numbers_tree.post_order_traversal()
    # iterative_post_order_tree = numbers_tree.iterative_post_order_traversal(numbers_tree)

   
    level_order_transvarsal = number_tree.level_order_traversal(number_tree)

    print(level_order_transvarsal)
    # print(in_order_tree)
    # print(iterative_in_order_traversal)
    # print(pre_order_tree)
    # print(iterative_pre_order_traversal)
    # print(post_order_tree)
    # print(iterative_post_order_tree)
    pass

if __name__ == '__main__':
    
    list = [15, 12, 27, 7, 14, 20, 88, 23]
    numbers_tree = build_binary_tree(list)
    
    traversal_algo(numbers_tree)