class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        curr_parent = self.parent

        while curr_parent:
            curr_parent = curr_parent.parent
            level += 1
        
        return level

    def print_tree(self):
        space = self.get_level() * "   "
        prefix = space + '|_' if self.parent else ""
        print(prefix, self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_product():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode('Mac'))
    laptop.add_child(TreeNode('Surface'))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixels"))

    root.add_child(laptop)
    root.add_child(cellphone)

    return root

if __name__ == '__main__':
    
    electronics_tree = build_product()
    electronics_tree.print_tree()

    

    