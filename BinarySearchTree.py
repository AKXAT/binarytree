class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self,data):
        if data == self.data:
            return
        if data<self.data:
            #add data in the left sub tree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
            #add data in the right sub tree
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
            #visiting the left tree
        #now add the root or the base node to the element list 
        elements.append(self.data)
        #now we need to visit the right sub tree
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    def search(self,value):
        if self.data == value:
            return True
        if value < self.data:
            #then the value might be in the left subtree
            if self.left:#to check if we have a left subtree
                return self.left.search(value)
            else:
                return False
            
        if value > self.data:
            #then the value might be in the right subtree
            if self.right:#to check if we have a right subtree
                return self.right.search(value)
            else:
                return False

def build_tree(element):
    root = BinarySearchTreeNode(element[0])
    for i in range(1,len(element)):
        root.add_child(element[i])
    return root

if __name__ == '__main__':
    numbers = [3,4,6,7,32,5,6,7,54,34,56]
    newtree  = build_tree(numbers)
    print(newtree.in_order_traversal())
    print(newtree.search(20))