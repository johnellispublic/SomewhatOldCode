class Vertex:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None

    def add_left_child(self, other):
        self.left_child = other
        other.parent = self

    def add_right_child(self, other):
        self.right_child = other
        other.parent = self
    
    def get_left_child(self):
        return self.left_child
    
    def get_right_child(self):
        return self.right_child

    def visit(self, end=' '):
        print(self.data, end=end)

    def traverse_inorder(self):
        if self.left_child is not None: 
            self.left_child.traverse_inorder()
        self.visit()
        if self.right_child is not None: 
            self.right_child.traverse_inorder()

    def traverse_preorder(self):
        self.visit()
        if self.left_child is not None:
            self.left_child.traverse_preorder()
        if self.right_child is not None:
            self.right_child.traverse_preorder()
    
    def traverse_postorder(self):
        if self.left_child is not None:
            self.left_child.traverse_postorder()
        if self.right_child is not None:
            self.right_child.traverse_postorder()
        self.visit()
    
    def has_right_child(self):
        return self.right_child is not None
    
    def has_left_child(self):
        return self.left_child is not None
    
    def __le__(self, other):
        if isinstance(other, Vertex):
            return self.data <= other.data
        else:
            return self.data <= other
    
    def __gt__(self, other):
        if isinstance(other, Vertex):
            return self.data > other.data
        else:
            return self.data > other




def create_binary_search_tree(arr):
    # Takes a list of integers and converts it to a BST. Returns the root of this BST (instance of Vertex)
    root = Vertex(arr[0])
    for number in arr[1:]:
        new_vertex = Vertex(number)
        parent = root
        while True:
            if new_vertex <= parent:
                if parent.has_left_child():
                    parent = parent.get_left_child()
                else:
                    parent.add_left_child(new_vertex)
                    break
            else:
                if parent.has_right_child():
                    parent = parent.get_right_child()
                else:
                    parent.add_right_child(new_vertex)
                    break
    return root


bst_root = create_binary_search_tree([ 21, 14, 35, 10, 12, 41, 26, 30, 39, 11, 44, 36])

print("Pre order:", end='\t')
bst_root.traverse_preorder()
print("\nIn order: ", end='\t')
bst_root.traverse_inorder()
print("\nPost order: ", end='\t')
bst_root.traverse_postorder()
print()


