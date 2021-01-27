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

def build_tree(element):
    root = BinarySearchTreeNode(element[0])
    for i in range(1,len(element)):
        root.add_child(element[i])
    return root

if __name__ == '__main__':
    numbers = [3,4,6,7,32,5,6,7,54,34,56]
    newtree  = build_tree(numbers)
    print(newtree.in_order_traversal())